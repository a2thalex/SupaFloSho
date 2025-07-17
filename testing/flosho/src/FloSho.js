import { chromium } from 'playwright';
import chalk from 'chalk';
import fs from 'fs/promises';
import path from 'path';
import { FlowRecorder } from './FlowRecorder.js';
import { APIVisualizer } from './APIVisualizer.js';
import { TestGenerator } from './TestGenerator.js';
import { PRPIntegration } from './PRPIntegration.js';

export class FloSho {
  constructor(projectName, options = {}) {
    this.projectName = projectName;
    this.options = {
      outputDir: options.outputDir || './testing/flosho-docs',
      viewport: options.viewport || { width: 1280, height: 720 },
      headless: options.headless ?? false,
      slowMo: options.slowMo || 50,
      prpPath: options.prpPath || './prp.json',
      ...options
    };
    
    this.browser = null;
    this.page = null;
    this.recorder = new FlowRecorder(this);
    this.apiViz = new APIVisualizer(this);
    this.generator = new TestGenerator(this);
    this.prp = new PRPIntegration(this);
  }

  async init() {
    console.log(chalk.blue.bold(`\n🌊 SupaFloSho Testing - ${this.projectName}\n`));
    
    // Load PRP if available
    await this.prp.loadPRP();
    
    this.browser = await chromium.launch({
      headless: this.options.headless,
      slowMo: this.options.slowMo
    });
    
    const context = await this.browser.newContext({
      viewport: this.options.viewport,
      recordVideo: {
        dir: path.join(this.options.outputDir, 'videos'),
        size: this.options.viewport
      }
    });
    
    // Intercept API calls for documentation
    await context.route('**/api/**', async (route, request) => {
      console.log(chalk.gray(`API Call: ${request.method()} ${request.url()}`));
      await route.continue();
    });
    
    this.page = await context.newPage();
    console.log(chalk.green('✅ SupaFloSho initialized - Ready to test!'));
    
    if (this.prp.hasPRP) {
      console.log(chalk.cyan('📄 PRP loaded - Test scenarios available'));
    }
  }

  async flow(flowName, steps) {
    // Check if flow exists in PRP
    const prpFlow = this.prp.getTestScenario(flowName);
    if (prpFlow) {
      console.log(chalk.magenta(`🎯 Using PRP scenario: ${flowName}`));
      steps = this.prp.mergeWithPRPScenario(steps, prpFlow);
    }
    
    return await this.recorder.recordFlow(flowName, steps);
  }

  async flowFromPRP(scenarioId) {
    const scenario = this.prp.getTestScenario(scenarioId);
    if (!scenario) {
      throw new Error(`PRP scenario '${scenarioId}' not found`);
    }
    
    console.log(chalk.magenta(`🎯 Running PRP scenario: ${scenario.name}`));
    return await this.recorder.recordFlow(scenario.name, scenario.steps);
  }

  async api(endpoint, tests) {
    // Check if API tests exist in PRP
    const prpTests = this.prp.getAPITests(endpoint);
    if (prpTests) {
      console.log(chalk.magenta(`🎯 Using PRP API tests for: ${endpoint}`));
      tests = [...tests, ...prpTests];
    }
    
    return await this.apiViz.testAPI(endpoint, tests);
  }

  async auto(featureName) {
    // Generate tests from PRP if available
    if (this.prp.hasPRP) {
      const prpFeature = this.prp.getFeature(featureName);
      if (prpFeature) {
        console.log(chalk.magenta(`🎯 Auto-generating tests from PRP: ${featureName}`));
        return await this.generator.autoTestFromPRP(prpFeature);
      }
    }
    
    return await this.generator.autoTest(featureName);
  }

  async validatePRP() {
    if (!this.prp.hasPRP) {
      console.log(chalk.yellow('⚠️ No PRP found - skipping validation'));
      return;
    }
    
    console.log(chalk.blue('\n🔍 Validating against PRP...'));
    const results = await this.prp.validateImplementation(this.recorder.flows);
    
    console.log(chalk.green(`✅ Covered: ${results.covered.length} scenarios`));
    if (results.missing.length > 0) {
      console.log(chalk.red(`❌ Missing: ${results.missing.length} scenarios`));
      results.missing.forEach(scenario => {
        console.log(chalk.red(`  - ${scenario}`));
      });
    }
    
    return results;
  }

  async setViewport(preset) {
    const viewports = {
      mobile: { width: 375, height: 667 },
      tablet: { width: 768, height: 1024 },
      desktop: { width: 1280, height: 720 },
      wide: { width: 1920, height: 1080 }
    };
    
    const viewport = viewports[preset] || preset;
    await this.page.setViewportSize(viewport);
    console.log(chalk.cyan(`📱 Viewport changed to: ${viewport.width}x${viewport.height}`));
  }

  async done() {
    console.log(chalk.yellow('\n📝 Generating documentation...'));
    
    // Validate PRP coverage
    const prpValidation = await this.validatePRP();
    
    await this.recorder.generateDocumentation();
    await this.apiViz.generateAPIDocs();
    
    if (this.browser) {
      await this.browser.close();
    }
    
    console.log(chalk.green.bold('\n✨ SupaFloSho testing complete!'));
    console.log(chalk.cyan(`📖 User Manual: ${this.options.outputDir}/user-manual/`));
    console.log(chalk.cyan(`📸 Screenshots: ${this.options.outputDir}/screenshots/`));
    console.log(chalk.cyan(`🎥 Videos: ${this.options.outputDir}/videos/`));
    
    if (prpValidation) {
      console.log(chalk.magenta(`🎯 PRP Coverage: ${prpValidation.coverage}%`));
    }
    
    // Generate summary
    const summary = {
      project: this.projectName,
      timestamp: new Date().toISOString(),
      flows: this.recorder.flows.length,
      screenshots: this.recorder.screenshots.length,
      apiTests: this.apiViz.apiTests.length,
      prpCoverage: prpValidation?.coverage || 'N/A',
      status: 'complete'
    };
    
    await fs.writeFile(
      path.join(this.options.outputDir, 'summary.json'),
      JSON.stringify(summary, null, 2)
    );
  }
}