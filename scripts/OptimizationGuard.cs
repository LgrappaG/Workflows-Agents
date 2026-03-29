using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.Bonus
{
    /// <summary>
    /// Extends the performance monitoring logic to provide proactive alerts and fixes.
    /// </summary>
    public class OptimizationGuard : MonoBehaviour
    {
        [Header("Thresholds")]
        public int maxBatches = 500;
        public int maxTriangles = 1000000;
        public float minFPS = 60f;
        public float reportCooldown = 5f;

        private PerformanceRecorder _recorder;
        private float _lastReportTime;

        private void Start()
        {
            _recorder = GetComponent<PerformanceRecorder>();
            if (_recorder == null) _recorder = gameObject.AddComponent<PerformanceRecorder>();
        }

        private void Update()
        {
            if (Time.time - _lastReportTime < reportCooldown) return;

            bool reported = false;
            if (_recorder.currentFPS < minFPS)
            {
                ReportBottleneck("FPS drop detected. Check for high GC or complex shaders.");
                reported = true;
            }

            if (_recorder.batches > maxBatches)
            {
                ReportBottleneck($"High Batch Count ({_recorder.batches}). Suggesting Static Batching or GPU Instancing.");
                reported = true;
            }

            if (reported)
            {
                _lastReportTime = Time.time;
            }
        }

        private void ReportBottleneck(string message)
        {
            // MCP looks for this specific log tag to trigger an audit
            Debug.LogWarning($"[MCP_OPTIMIZATION_ALERT] {message}");
        }
    }
}
