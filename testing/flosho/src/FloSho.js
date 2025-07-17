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
    console.log(chalk.blue.bold(`\n🌊 FloSho Testing - ${this.projectName}`));
    console.log(chalk.gray('Part of SupaFloSho Framework\n'));
    
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
    console.log(chalk.green('✅ FloSho initialized - Ready to test!'));
    
    if (this.prp.hasPRP) {
      console.log(chalk.cyan('📋 PRP loaded - Test scenarios available'));
    }
  }

  async flow(flowName, steps) {
    // If no steps provided, try to load from PRP
    if (!steps && this.prp.hasPRP) {
      steps = await this.prp.getFlowSteps(flowName);
      if (steps) {
        console.log(chalk.cyan(`📋 Using PRP test scenario: ${flowName}`));
      }
    }
    
    return await this.recorder.recordFlow(flowName, steps);
  }

  async api(endpoint, tests) {
    // If no tests provided, try to load from PRP
    if (!tests && this.prp.hasPRP) {
      tests = await this.prp.getAPITests(endpoint);
      if (tests) {
        console.log(chalk.cyan(`📋 Using PRP API tests for: ${endpoint}`));
      }
    }
    
    return await this.apiViz.testAPI(endpoint, tests);
  }

  async auto(featureName) {
    // Enhanced auto-test with PRP integration
    const prpScenarios = await this.prp.getFeatureScenarios(featureName);
    if (prpScenarios) {
      console.log(chalk.cyan(`📋 Auto-testing ${prpScenarios.length} PRP scenarios`));
      return await this.generator.autoTestWithPRP(featureName, prpScenarios);
    }
    
    return await this.generator.autoTest(featureName);
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

  async validateAgainstPRP() {
    if (!this.prp.hasPRP) {
      console.log(chalk.yellow('⚠️  No PRP found for validation'));
      return;
    }
    
    console.log(chalk.blue('\n🔍 Validating test coverage against PRP...'));
    const report = await this.prp.validateCoverage(
      this.recorder.flows,
      this.apiViz.apiTests
    );
    
    console.log(chalk.green(`✅ Coverage: ${report.coverage}%`));
    if (report.missing.length > 0) {
      console.log(chalk.yellow('⚠️  Missing test scenarios:'));
      report.missing.forEach(scenario => {
        console.log(chalk.yellow(`   - ${scenario}`));
      });
    }
    
    return report;
  }

  async done() {
    console.log(chalk.yellow('\n📝 Generating documentation...'));
    
    // Generate standard documentation
    await this.recorder.generateDocumentation();
    await this.apiViz.generateAPIDocs();
    
    // Generate PRP compliance report
    const prpReport = await this.validateAgainstPRP();
    
    if (this.browser) {
      await this.browser.close();
    }
    
    console.log(chalk.green.bold('\n✨ FloSho testing complete!'));
    console.log(chalk.cyan(`📖 User Manual: ${this.options.outputDir}/user-manual/`));
    console.log(chalk.cyan(`📸 Screenshots: ${this.options.outputDir}/screenshots/`));
    console.log(chalk.cyan(`🎥 Videos: ${this.options.outputDir}/videos/`));
    console.log(chalk.cyan(`📋 PRP Report: ${this.options.outputDir}/prp-compliance.json`));
    
    // Generate summary
    const summary = {
      project: this.projectName,
      framework: 'SupaFloSho',
      timestamp: new Date().toISOString(),
      flows: this.recorder.flows.length,
      screenshots: this.recorder.screenshots.length,
      apiTests: this.apiViz.apiTests.length,
      prpCompliance: prpReport,
      status: 'complete'
    };
    
    await fs.writeFile(
      path.join(this.options.outputDir, 'summary.json'),
      JSON.stringify(summary, null, 2)
    );
  }
}