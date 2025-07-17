import fs from 'fs/promises';
import path from 'path';
import chalk from 'chalk';

/**
 * PRP Integration for SupaFloSho
 * Connects FloSho testing with xText-PRP requirements
 */
export class PRPIntegration {
  constructor(flosho) {
    this.flosho = flosho;
    this.prp = null;
    this.hasPRP = false;
  }

  async loadPRP() {
    try {
      const prpPath = this.flosho.options.prpPath;
      const prpContent = await fs.readFile(prpPath, 'utf-8');
      this.prp = JSON.parse(prpContent);
      this.hasPRP = true;
      console.log(chalk.green(`✅ PRP loaded from: ${prpPath}`));
    } catch (error) {
      // PRP is optional, so we don't throw
      console.log(chalk.gray('No PRP found - testing without requirements'));
    }
  }

  getTestScenario(name) {
    if (!this.hasPRP || !this.prp.testScenarios) return null;
    
    return this.prp.testScenarios.find(scenario => 
      scenario.name === name || scenario.id === name
    );
  }

  getAPITests(endpoint) {
    if (!this.hasPRP || !this.prp.apiTests) return [];
    
    return this.prp.apiTests.filter(test => 
      test.endpoint === endpoint || endpoint.includes(test.endpoint)
    );
  }

  getFeature(featureName) {
    if (!this.hasPRP || !this.prp.features) return null;
    
    return this.prp.features.find(feature => 
      feature.name === featureName || feature.id === featureName
    );
  }

  getUserStories() {
    if (!this.hasPRP || !this.prp.userStories) return [];
    return this.prp.userStories;
  }

  getAcceptanceCriteria(storyId) {
    const story = this.getUserStories().find(s => s.id === storyId);
    return story?.acceptanceCriteria || [];
  }

  mergeWithPRPScenario(userSteps, prpScenario) {
    // Merge user-provided steps with PRP scenario
    // PRP provides the structure, user can override specifics
    const merged = [];
    
    prpScenario.steps.forEach((prpStep, index) => {
      const userStep = userSteps[index];
      if (userStep) {
        // User step takes precedence but inherits PRP metadata
        merged.push({
          ...prpStep,
          ...userStep,
          prpValidation: prpStep.validation
        });
      } else {
        // Use PRP step as-is
        merged.push(prpStep);
      }
    });
    
    // Add any extra user steps
    if (userSteps.length > prpScenario.steps.length) {
      merged.push(...userSteps.slice(prpScenario.steps.length));
    }
    
    return merged;
  }

  async validateImplementation(executedFlows) {
    if (!this.hasPRP || !this.prp.testScenarios) {
      return { covered: [], missing: [], coverage: 100 };
    }
    
    const requiredScenarios = this.prp.testScenarios.map(s => s.name);
    const executedScenarios = executedFlows.map(f => f.name);
    
    const covered = requiredScenarios.filter(scenario => 
      executedScenarios.includes(scenario)
    );
    
    const missing = requiredScenarios.filter(scenario => 
      !executedScenarios.includes(scenario)
    );
    
    const coverage = Math.round((covered.length / requiredScenarios.length) * 100);
    
    return { covered, missing, coverage };
  }

  generateTestsFromUserStory(story) {
    const tests = [];
    
    // Generate a main flow test
    tests.push({
      name: `User Story: ${story.title}`,
      steps: story.acceptanceCriteria.map(criteria => ({
        action: 'validate',
        description: criteria,
        validation: true
      }))
    });
    
    // Generate edge case tests if defined
    if (story.edgeCases) {
      story.edgeCases.forEach(edgeCase => {
        tests.push({
          name: `Edge Case: ${edgeCase.name}`,
          steps: edgeCase.steps
        });
      });
    }
    
    return tests;
  }

  async exportPRPValidationReport(outputPath) {
    const report = {
      project: this.flosho.projectName,
      prpVersion: this.prp?.version || 'unknown',
      timestamp: new Date().toISOString(),
      userStories: this.getUserStories().map(story => ({
        id: story.id,
        title: story.title,
        tested: this.flosho.recorder.flows.some(flow => 
          flow.name.includes(story.title) || flow.metadata?.storyId === story.id
        )
      })),
      testScenarios: this.prp?.testScenarios?.map(scenario => ({
        id: scenario.id,
        name: scenario.name,
        executed: this.flosho.recorder.flows.some(flow => flow.name === scenario.name)
      })) || [],
      overallCoverage: 0 // Will be calculated
    };
    
    // Calculate overall coverage
    const totalItems = report.userStories.length + report.testScenarios.length;
    const testedItems = report.userStories.filter(s => s.tested).length + 
                       report.testScenarios.filter(s => s.executed).length;
    report.overallCoverage = totalItems > 0 ? Math.round((testedItems / totalItems) * 100) : 0;
    
    await fs.writeFile(outputPath, JSON.stringify(report, null, 2));
    
    return report;
  }
}
