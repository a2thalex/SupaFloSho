/**
 * SupaFloSho Todo App Example
 * This demonstrates the complete workflow integration
 */

import { FloSho } from '../../testing/flosho/index.js';
import chalk from 'chalk';

// Configuration
const config = {
  projectName: 'todo-app',
  baseUrl: process.env.TODO_APP_URL || 'http://localhost:3000',
  prpPath: './todo-app-prp.json'
};

async function runExample() {
  console.log(chalk.bold.cyan('\n🌊 SupaFloSho Todo App Example\n'));
  console.log(chalk.gray('Demonstrating xText-PRP + SuperClaude + FloSho integration\n'));
  
  // Initialize FloSho with PRP
  const flosho = new FloSho(config.projectName, {
    prpPath: config.prpPath,
    outputDir: './test-results',
    headless: false,
    slowMo: 100
  });
  
  await flosho.init();
  
  // Step 1: Run PRP-defined test scenarios
  console.log(chalk.blue('\n1️⃣  Running PRP Test Scenarios'));
  console.log(chalk.gray('   FloSho reads test scenarios from PRP...\n'));
  
  // This automatically uses the PRP test scenario!
  await flosho.flow('Complete Todo Workflow');
  
  // Step 2: Test additional flows
  console.log(chalk.blue('\n2️⃣  Testing Category Management'));
  
  await flosho.flow('Category Management', [
    { action: 'navigate', url: `${config.baseUrl}/categories` },
    { action: 'screenshot', name: 'categories-page' },
    { action: 'click', selector: '#new-category' },
    { action: 'fill', selector: '#category-name', value: 'Personal' },
    { action: 'fill', selector: '#category-color', value: '#ff5722' },
    { action: 'click', selector: '#save-category' },
    { action: 'screenshot', name: 'category-created' }
  ]);
  
  // Step 3: Test real-time collaboration
  console.log(chalk.blue('\n3️⃣  Testing Real-time Collaboration'));
  
  await flosho.flow('Team Collaboration', [
    { action: 'navigate', url: `${config.baseUrl}/team` },
    { action: 'screenshot', name: 'team-dashboard' },
    { action: 'click', selector: '#invite-member' },
    { action: 'fill', selector: '#email-input', value: 'teammate@example.com' },
    { action: 'click', selector: '#send-invite' },
    { action: 'screenshot', name: 'invite-sent' },
    { action: 'wait', duration: 2000, description: 'Wait for real-time update' },
    { action: 'screenshot', name: 'member-joined' }
  ]);
  
  // Step 4: Test API endpoints from PRP
  console.log(chalk.blue('\n4️⃣  Testing API Endpoints (from PRP)'));
  
  await flosho.api('/api/todos', [
    {
      name: 'Get all todos',
      method: 'GET',
      expect: { status: 200 }
    },
    {
      name: 'Create todo',
      method: 'POST',
      data: {
        title: 'Test todo from FloSho',
        description: 'Created during automated testing',
        category: 'Work'
      },
      expect: { 
        status: 201,
        body: { title: 'Test todo from FloSho' }
      }
    },
    {
      name: 'Update todo',
      method: 'PUT',
      endpoint: '/api/todos/1',
      data: { completed: true },
      expect: { status: 200 }
    }
  ]);
  
  // Step 5: Validate against PRP
  console.log(chalk.blue('\n5️⃣  Validating Coverage Against PRP'));
  
  const prpReport = await flosho.validateAgainstPRP();
  
  // Step 6: Generate documentation
  console.log(chalk.blue('\n6️⃣  Generating Documentation'));
  
  await flosho.done();
  
  // Summary
  console.log(chalk.green.bold('\n✨ SupaFloSho Example Complete!\n'));
  console.log(chalk.white('What just happened:'));
  console.log(chalk.gray('1. FloSho read test scenarios from the PRP'));
  console.log(chalk.gray('2. Executed visual tests with screenshots'));
  console.log(chalk.gray('3. Tested APIs matching PRP specifications'));
  console.log(chalk.gray('4. Validated coverage against requirements'));
  console.log(chalk.gray('5. Generated complete documentation\n'));
  
  console.log(chalk.cyan('Check the results:'));
  console.log(chalk.cyan('📖 User Guide: ./test-results/user-manual/'));
  console.log(chalk.cyan('📸 Screenshots: ./test-results/screenshots/'));
  console.log(chalk.cyan('📋 PRP Report: ./test-results/prp-compliance.json\n'));
}

// Run the example
runExample().catch(console.error);