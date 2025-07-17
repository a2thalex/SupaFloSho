/**
 * PRP Integration for FloSho
 * Connects FloSho testing with xText-PRP requirements
 */

import fs from 'fs/promises';
import path from 'path';
import chalk from 'chalk';

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
      console.log(chalk.green('✅ PRP loaded successfully'));
    } catch (error) {
      // PRP is optional, so no error if not found
      this.hasPRP = false;
    }
  }

  async getFlowSteps(flowName) {
    if (!this.hasPRP || !this.prp.testScenarios) return null;
    
    // Find matching test scenario in PRP
    const scenario = this.prp.testScenarios.find(
      s => s.name === flowName || s.id === flowName
    );
    
    if (!scenario) return null;
    
    // Convert PRP scenario to FloSho steps
    return scenario.steps.map(step => ({
      action: step.action,
      selector: step.selector || step.element,
      value: step.value || step.data,
      description: step.description,
      expected: step.expected
    }));
  }

  async getAPITests(endpoint) {
    if (!this.hasPRP || !this.prp.apiSpecifications) return null;
    
    // Find matching API spec in PRP
    const apiSpec = this.prp.apiSpecifications.find(
      spec => spec.endpoint === endpoint || spec.path === endpoint
    );
    
    if (!apiSpec) return null;
    
    // Convert PRP API spec to FloSho tests
    return apiSpec.tests || [
      {
        name: `Test ${apiSpec.method} ${endpoint}`,
        method: apiSpec.method,
        data: apiSpec.exampleRequest,
        expect: {
          status: apiSpec.expectedStatus || 200,
          schema: apiSpec.responseSchema
        }
      }
    ];
  }

  async getFeatureScenarios(featureName) {
    if (!this.hasPRP || !this.prp.features) return null;
    
    // Find feature in PRP
    const feature = this.prp.features.find(
      f => f.name === featureName || f.id === featureName
    );
    
    if (!feature || !feature.scenarios) return null;
    
    return feature.scenarios;
  }

  async validateCoverage(flows, apiTests) {
    if (!this.hasPRP) {
      return { coverage: 100, missing: [], status: 'no-prp' };
    }
    
    const report = {
      coverage: 0,
      missing: [],
      covered: [],
      total: 0
    };
    
    // Check test scenario coverage
    if (this.prp.testScenarios) {
      report.total += this.prp.testScenarios.length;
      
      this.prp.testScenarios.forEach(scenario => {
        const covered = flows.some(flow => 
          flow.name === scenario.name || flow.name === scenario.id
        );
        
        if (covered) {
          report.covered.push(scenario.name);
        } else {
          report.missing.push(`Test Scenario: ${scenario.name}`);
        }
      });
    }
    
    // Check API coverage
    if (this.prp.apiSpecifications) {
      report.total += this.prp.apiSpecifications.length;
      
      this.prp.apiSpecifications.forEach(apiSpec => {
        const covered = apiTests.some(test => 
          test.endpoint === apiSpec.endpoint || test.endpoint === apiSpec.path
        );
        
        if (covered) {
          report.covered.push(`API: ${apiSpec.endpoint}`);
        } else {
          report.missing.push(`API Test: ${apiSpec.method} ${apiSpec.endpoint}`);
        }
      });
    }
    
    // Calculate coverage percentage
    report.coverage = report.total > 0 
      ? Math.round((report.covered.length / report.total) * 100)
      : 100;
    
    // Save report
    await fs.writeFile(
      path.join(this.flosho.options.outputDir, 'prp-compliance.json'),
      JSON.stringify(report, null, 2)
    );
    
    return report;
  }
}