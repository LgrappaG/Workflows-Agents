#!/usr/bin/env node

/**
 * Analytics Dashboard Setup
 *
 * Initializes analytics infrastructure:
 * - Event schema validation
 * - Dashboard configuration
 * - Sample event generation for testing
 * - Real-time metrics aggregation
 *
 * Usage: node scripts/analytics-setup.js [--generate-samples] [--start-dashboard]
 */

const fs = require('fs');
const path = require('path');
const http = require('http');

const projectRoot = path.join(__dirname, '..');

// ============================================================================
// 1. Event Schema Definition
// ============================================================================

const eventSchema = {
  skill_discovered: {
    required: ['userId', 'skillId', 'source', 'timestamp'],
    optional: ['domain', 'searchQuery', 'referrer'],
    description: 'User discovers a skill via search, browse, or recommendation'
  },
  skill_adopted: {
    required: ['userId', 'skillId', 'workflowId', 'timestamp'],
    optional: ['previousSkills', 'adoptedWithVariant'],
    description: 'User officially adopts a skill into their workflow'
  },
  workflow_created: {
    required: ['userId', 'workflowId', 'skillIds', 'timestamp'],
    optional: ['templateId', 'clonedFrom'],
    description: 'User creates a new workflow combining multiple skills'
  },
  workflow_completed: {
    required: ['userId', 'workflowId', 'duration', 'timestamp'],
    optional: ['successMetrics', 'errors', 'fallbacksUsed'],
    description: 'User completes a full workflow execution'
  },
  skill_shared: {
    required: ['userId', 'skillId', 'recipientId', 'timestamp'],
    optional: ['channel', 'feedback'],
    description: 'User shares skill with colleague/team'
  },
  validation_run: {
    required: ['skillId', 'gatesPassed', 'gatesFailed', 'timestamp'],
    optional: ['duration', 'checksPerformed'],
    description: 'Skill validation gate execution result'
  },
  benchmark_recorded: {
    required: ['skillId', 'metric', 'value', 'timestamp'],
    optional: ['hardware', 'variant'],
    description: 'Performance benchmark metric recorded'
  },
  error_reported: {
    required: ['skillId', 'userId', 'errorType', 'timestamp'],
    optional: ['stackTrace', 'environment', 'severity'],
    description: 'User reports error in skill or workflow'
  }
};

// ============================================================================
// 2. Dashboard Configuration
// ============================================================================

const dashboardConfig = {
  title: '.agents Analytics Dashboard',
  refreshInterval: 5000, // ms
  metrics: [
    {
      id: 'skills_discovered_24h',
      name: 'Skills Discovered (24h)',
      type: 'counter',
      event: 'skill_discovered',
      timeWindow: '24h',
      target: '>100'
    },
    {
      id: 'adoption_rate',
      name: 'Adoption Rate',
      type: 'percentage',
      formula: 'skill_adopted / skill_discovered',
      timeWindow: '7d',
      target: '>30%'
    },
    {
      id: 'workflow_completion_rate',
      name: 'Workflow Completion',
      type: 'percentage',
      formula: 'workflow_completed / workflow_created',
      timeWindow: '7d',
      target: '>80%'
    },
    {
      id: 'validation_pass_rate',
      name: 'Validation Pass Rate',
      type: 'percentage',
      formula: 'gatesPassed / (gatesPassed + gatesFailed)',
      timeWindow: '24h',
      target: '>99%'
    },
    {
      id: 'avg_workflow_duration',
      name: 'Avg Workflow Duration',
      type: 'duration',
      metric: 'workflow_completed.duration',
      aggregation: 'average',
      timeWindow: '7d',
      target: '<5 minutes'
    },
    {
      id: 'error_rate',
      name: 'Error Rate',
      type: 'percentage',
      event: 'error_reported',
      timeWindow: '24h',
      target: '<5%'
    },
    {
      id: 'top_skills_24h',
      name: 'Top Skills (24h Discoveries)',
      type: 'leaderboard',
      event: 'skill_discovered',
      groupBy: 'skillId',
      limit: 10
    },
    {
      id: 'skill_sharing_network',
      name: 'Sharing Network',
      type: 'graph',
      event: 'skill_shared',
      nodes: 'userId',
      edges: 'skillId'
    }
  ]
};

// ============================================================================
// 3. Sample Event Generation (for testing)
// ============================================================================

function generateSampleEvents(count = 100) {
  const events = [];
  const skillIds = [
    'ai-llm-runtime-integration',
    'ml-model-serving-unity',
    'cross-engine-portability-layer',
    'community-marketplace-governance',
    'analytics-funnel-attribution',
    'benchmark-regression-gates'
  ];
  const userIds = Array.from({length: 50}, (_, i) => `user-${i+1}`);
  const sources = ['search', 'browse', 'recommendation', 'community'];

  for (let i = 0; i < count; i++) {
    const eventType = ['skill_discovered', 'skill_adopted', 'workflow_created', 'workflow_completed'][
      Math.floor(Math.random() * 4)
    ];
    const timestamp = new Date(Date.now() - Math.random() * 24 * 60 * 60 * 1000).toISOString();

    let event = {
      eventType,
      timestamp,
      userId: userIds[Math.floor(Math.random() * userIds.length)],
      skillId: skillIds[Math.floor(Math.random() * skillIds.length)]
    };

    if (eventType === 'skill_discovered') {
      event.source = sources[Math.floor(Math.random() * sources.length)];
      event.domain = Math.random() > 0.5 ? 'game-dev' : 'game-engines';
    } else if (eventType === 'skill_adopted') {
      event.workflowId = `workflow-${Math.floor(Math.random() * 100)}`;
    } else if (eventType === 'workflow_created') {
      event.workflowId = `workflow-${Math.floor(Math.random() * 100)}`;
      event.skillIds = [skillIds[Math.floor(Math.random() * skillIds.length)]];
    } else if (eventType === 'workflow_completed') {
      event.workflowId = `workflow-${Math.floor(Math.random() * 100)}`;
      event.duration = Math.floor(Math.random() * 600 * 1000); // 0-10 minutes
    }

    events.push(event);
  }

  return events;
}

// ============================================================================
// 4. Analytics Storage & Aggregation
// ============================================================================

class AnalyticsStore {
  constructor() {
    this.events = [];
    this.aggregates = {};
  }

  addEvent(event) {
    this.events.push(event);
  }

  addEvents(events) {
    this.events.push(...events);
  }

  computeMetrics(timeWindowHours = 24) {
    const cutoff = Date.now() - timeWindowHours * 60 * 60 * 1000;
    const recentEvents = this.events.filter(e => new Date(e.timestamp).getTime() > cutoff);

    const metrics = {
      totalEvents: recentEvents.length,
      eventsByType: {},
      discoveryCount: 0,
      adoptionCount: 0,
      adoptionRate: 0,
      completionRate: 0,
      validationPassRate: 0.99,
      topSkills: {},
      errorRate: 0
    };

    for (const event of recentEvents) {
      metrics.eventsByType[event.eventType] = (metrics.eventsByType[event.eventType] || 0) + 1;

      if (event.eventType === 'skill_discovered') metrics.discoveryCount++;
      if (event.eventType === 'skill_adopted') metrics.adoptionCount++;
    }

    if (metrics.discoveryCount > 0) {
      metrics.adoptionRate = ((metrics.adoptionCount / metrics.discoveryCount) * 100).toFixed(1);
    }

    // Skill rankings
    for (const event of recentEvents) {
      if (event.skillId) {
        metrics.topSkills[event.skillId] = (metrics.topSkills[event.skillId] || 0) + 1;
      }
    }

    return metrics;
  }

  generateReport() {
    const metrics24h = this.computeMetrics(24);
    const metrics7d = this.computeMetrics(24 * 7);

    return {
      generated: new Date().toISOString(),
      timeRanges: {
        '24h': metrics24h,
        '7d': metrics7d
      },
      topSkills: Object.entries(metrics24h.topSkills)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10)
    };
  }
}

// ============================================================================
// 5. dashboard HTTP Server
// ============================================================================

function startDashboard(store, port = 5000) {
  const server = http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Content-Type', 'application/json');

    if (req.url === '/api/metrics') {
      const metrics = store.computeMetrics(24);
      res.writeHead(200);
      res.end(JSON.stringify(metrics, null, 2));
    } else if (req.url === '/api/report') {
      const report = store.generateReport();
      res.writeHead(200);
      res.end(JSON.stringify(report, null, 2));
    } else if (req.url === '/api/config') {
      res.writeHead(200);
      res.end(JSON.stringify(dashboardConfig, null, 2));
    } else if (req.url === '/') {
      const html = `<!DOCTYPE html>
<html>
<head>
  <title>.agents Analytics Dashboard</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; padding: 20px; background: #1e1e1e; color: #e0e0e0; }
    .container { max-width: 1200px; margin: 0 auto; }
    h1 { color: #4fc3f7; }
    .metrics { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 20px 0; }
    .metric { background: #2a2a2a; padding: 15px; border-radius: 8px; border-left: 4px solid #4fc3f7; }
    .metric-value { font-size: 28px; font-weight: bold; color: #4fc3f7; }
    .metric-label { font-size: 12px; color: #888; margin-top: 5px; }
    .status-ok { color: #81c784; }
    .status-warning { color: #ffa726; }
    .status-error { color: #e57373; }
    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
    th, td { padding: 10px; text-align: left; border-bottom: 1px solid #3a3a3a; }
    th { background: #2a2a2a; font-weight: bold; }
  </style>
  <script>
    async function updateDashboard() {
      const metrics = await fetch('/api/metrics').then(r => r.json());
      const report = await fetch('/api/report').then(r => r.json());

      document.getElementById('total-events').textContent = metrics.totalEvents;
      document.getElementById('discovery-count').textContent = metrics.discoveryCount;
      document.getElementById('adoption-rate').textContent = metrics.adoptionRate + '%';

      const skillsList = report.topSkills.map(([skill, count]) =>
        \`<tr><td>\${skill}</td><td>\${count}</td></tr>\`
      ).join('');

      document.getElementById('skills-table').innerHTML = skillsList;
    }

    updateDashboard();
    setInterval(updateDashboard, 5000);
  </script>
</head>
<body>
  <div class="container">
    <h1>📊 .agents Analytics Dashboard</h1>
    <p>Real-time metrics for skill adoption, workflow completion, and platform health.</p>

    <div class="metrics">
      <div class="metric">
        <div class="metric-value" id="total-events">-</div>
        <div class="metric-label">Total Events (24h)</div>
      </div>
      <div class="metric">
        <div class="metric-value" id="discovery-count">-</div>
        <div class="metric-label">Skills Discovered</div>
      </div>
      <div class="metric">
        <div class="metric-value" id="adoption-rate">-</div>
        <div class="metric-label">Adoption Rate</div>
      </div>
    </div>

    <h2>Top Skills (24h)</h2>
    <table>
      <thead>
        <tr><th>Skill</th><th>Discoveries</th></tr>
      </thead>
      <tbody id="skills-table">
        <tr><td colspan="2">Loading...</td></tr>
      </tbody>
    </table>

    <p style="color: #666; font-size: 12px;">Last updated: <span id="timestamp"></span></p>
  </div>
  <script>
    document.getElementById('timestamp').textContent = new Date().toLocaleString();
  </script>
</body>
</html>`;
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.end(html);
    } else {
      res.writeHead(404);
      res.end(JSON.stringify({error: 'not found'}));
    }
  });

  server.listen(port, () => {
    console.log(`[analytics-dashboard] server=http://localhost:${port}`);
  });

  return server;
}

// ============================================================================
// 6. Main Execution
// ============================================================================

function main() {
  const args = process.argv.slice(2);
  const generateSamples = args.includes('--generate-samples');
  const startServer = args.includes('--start-dashboard');

  console.log('[analytics-setup] phase=initialization');

  // Write event schema
  const schemaPath = path.join(projectRoot, 'data', 'event-schema.json');
  fs.mkdirSync(path.dirname(schemaPath), { recursive: true });
  fs.writeFileSync(schemaPath, JSON.stringify(eventSchema, null, 2));
  console.log(`[analytics-setup] schema=${schemaPath}`);

  // Write dashboard config
  const configPath = path.join(projectRoot, 'data', 'dashboard-config.json');
  fs.writeFileSync(configPath, JSON.stringify(dashboardConfig, null, 2));
  console.log(`[analytics-setup] config=${configPath}`);

  // Initialize store
  const store = new AnalyticsStore();

  // Generate sample events if requested
  if (generateSamples) {
    const samples = generateSampleEvents(150);
    store.addEvents(samples);
    const samplesPath = path.join(projectRoot, 'reports', 'analytics', 'sample-events.json');
    fs.mkdirSync(path.dirname(samplesPath), { recursive: true });
    fs.writeFileSync(samplesPath, JSON.stringify(samples, null, 2));
    console.log(`[analytics-setup] samples=150 path=${samplesPath}`);
  }

  // Generate initial report
  const report = store.generateReport();
  const reportPath = path.join(projectRoot, 'reports', 'analytics', 'initial-report.json');
  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
  console.log(`[analytics-setup] report=${reportPath}`);

  // Start dashboard server if requested
  if (startServer) {
    startDashboard(store);
  }

  console.log(`[analytics-setup] complete=true`);
}

main();