using UnityEngine;
using System.Collections.Generic;
using System;

#if UNITY_ANALYTICS
using Unity.Services.Analytics;
#endif

namespace Antigravity.Analytics
{
    /// <summary>
    /// Centralized telemetry and event tracking system.
    /// Supports Firebase Analytics, Amplitude, and custom backends.
    /// Automatic crash reporting, performance metrics, and user behavior tracking.
    /// </summary>
    public class TelemetryCollector : MonoBehaviour
    {
        public static TelemetryCollector Instance { get; private set; }

        [SerializeField]
        private bool _enableTracking = true;

        [SerializeField]
        private bool _enableCrashReporting = true;

        private Dictionary<string, object> _customMetadata = new();
        private float _sessionStartTime;

        public delegate void OnEventLogged(string eventName, Dictionary<string, object> parameters);
        public event OnEventLogged EventLogged;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }

            Instance = this;
            DontDestroyOnLoad(gameObject);
        }

        private void Start()
        {
            _sessionStartTime = Time.realtimeSinceStartup;
            InitializeAnalytics();
            LogEvent("app_started", new Dictionary<string, object>
            {
                { "device_model", SystemInfo.deviceModel },
                { "os_version", SystemInfo.operatingSystem },
                { "ram_mb", SystemInfo.systemMemorySize }
            });
        }

        /// <summary>
        /// Initialize analytics platform (Firebase, Amplitude, etc).
        /// </summary>
        private void InitializeAnalytics()
        {
            if (!_enableTracking) return;

#if UNITY_ANALYTICS
            // Firebase initialization handled by SDK auto-init
            Debug.Log("[Analytics] Firebase Analytics initialized");
#endif
        }

        /// <summary>
        /// Log custom event with parameters.
        /// </summary>
        public void LogEvent(string eventName, Dictionary<string, object> parameters = null)
        {
            if (!_enableTracking) return;

            parameters ??= new();
            parameters["timestamp"] = DateTime.UtcNow.ToString("yyyy-MM-dd'T'HH:mm:ss'Z'");

            Debug.Log($"[Analytics] Event: {eventName} | Params: {string.Join(", ", parameters)}");
            EventLogged?.Invoke(eventName, parameters);

#if UNITY_ANALYTICS
            var paramArray = parameters
                .Select(p => new Firebase.Analytics.Parameter(p.Key, p.Value))
                .ToArray();
            Firebase.Analytics.FirebaseAnalytics.LogEvent(eventName, paramArray);
#endif
        }

        /// <summary>
        /// Log gameplay milestone event.
        /// </summary>
        public void LogGameplayEvent(string action, string target, int value = 0)
        {
            LogEvent($"gameplay_{action}", new Dictionary<string, object>
            {
                { "target", target },
                { "value", value },
                { "session_time_sec", (int)(Time.realtimeSinceStartup - _sessionStartTime) }
            });
        }

        /// <summary>
        /// Log monetization event (in-app purchase).
        /// </summary>
        public void LogPurchase(string itemId, double price, string currency = "USD")
        {
            LogEvent("purchase", new Dictionary<string, object>
            {
                { "item_id", itemId },
                { "value", price },
                { "currency", currency }
            });
        }

        /// <summary>
        /// Log progression event (level, achievement, milestone).
        /// </summary>
        public void LogProgression(string progressionType, string progressionName, int level)
        {
            LogEvent("progression", new Dictionary<string, object>
            {
                { "type", progressionType },
                { "name", progressionName },
                { "level", level }
            });
        }

        /// <summary>
        /// Log performance metrics (FPS, memory, etc).
        /// </summary>
        public void LogPerformanceMetrics()
        {
            long heap = System.GC.GetTotalMemory(false) / 1024 / 1024;
            LogEvent("performance_metrics", new Dictionary<string, object>
            {
                { "fps", Time.frameCount / Time.realtimeSinceStartup },
                { "heap_mb", heap },
                { "gc_count", System.GC.CollectionCount(0) }
            });
        }

        /// <summary>
        /// Set custom user property (for segmentation).
        /// </summary>
        public void SetUserProperty(string key, string value)
        {
            _customMetadata[key] = value;
            Debug.Log($"[Analytics] User property: {key} = {value}");

#if UNITY_ANALYTICS
            Firebase.Analytics.FirebaseAnalytics.SetUserProperty(key, value);
#endif
        }

        /// <summary>
        /// Report exception for crash analytics.
        /// </summary>
        public void ReportException(System.Exception ex, string context = "")
        {
            if (!_enableCrashReporting) return;

            Debug.LogError($"[Analytics] Exception: {ex.GetType().Name} | {ex.Message}\nContext: {context}");

#if UNITY_ANALYTICS
            var properties = new Dictionary<string, object>
            {
                { "message", ex.Message },
                { "stacktrace", ex.StackTrace },
                { "context", context }
            };
            var paramArray = properties
                .Select(p => new Firebase.Analytics.Parameter(p.Key, p.Value.ToString()))
                .ToArray();
            Firebase.Analytics.FirebaseAnalytics.LogEvent("exception_report", paramArray);
#endif
        }

        /// <summary>
        /// Log session end (cleanup, final metrics).
        /// </summary>
        public void LogSessionEnd()
        {
            float sessionDuration = Time.realtimeSinceStartup - _sessionStartTime;
            LogEvent("session_end", new Dictionary<string, object>
            {
                { "duration_sec", (int)sessionDuration },
                { "frames_rendered", Time.frameCount }
            });
        }

        private void OnApplicationQuit()
        {
            LogSessionEnd();
        }
    }
}
