using UnityEngine;
using UnityEngine.Profiling;
using System.Text;

/// <summary>
/// Captures real-time performance data and exposes it for AI-led MCP audits.
/// Attach this to a persistent GameObject in your initial scene.
/// </summary>
public class PerformanceRecorder : MonoBehaviour
{
    [Header("Settings")]
    public float updateInterval = 1.0f;
    public bool logToConsole = true;

    [Header("Live Stats (Read-Only)")]
    public float currentFPS;
    public long gcAllocatedMemory;
    public int batches;
    public int triangles;

    private float _timer;
    private StringBuilder _logBuilder = new StringBuilder();

    void Update()
    {
        _timer += Time.deltaTime;
        if (_timer >= updateInterval)
        {
            CaptureStats();
            if (logToConsole) LogStats();
            _timer = 0;
        }
    }

    private void CaptureStats()
    {
        currentFPS = 1.0f / Time.smoothDeltaTime;
        gcAllocatedMemory = Profiler.GetTotalAllocatedMemoryLong() / (1024 * 1024); // MB

        // Note: Batches and Triangles require UnityEditor.UnityStats for accurate Editor-time stats,
        // but for runtime we can use Profiler counters if available.
#if UNITY_EDITOR
        batches = UnityEditor.UnityStats.batches;
        triangles = UnityEditor.UnityStats.triangles;
#endif
    }

    private void LogStats()
    {
        _logBuilder.Clear();
        _logBuilder.AppendLine("[MCP_PERF_STAT]");
        _logBuilder.AppendLine($"FPS: {currentFPS:F1}");
        _logBuilder.AppendLine($"Memory: {gcAllocatedMemory} MB");
        _logBuilder.AppendLine($"Batches: {batches}");
        _logBuilder.AppendLine($"Triangles: {triangles}");

        Debug.Log(_logBuilder.ToString());
    }
}
