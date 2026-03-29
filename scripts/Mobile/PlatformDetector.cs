using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.Mobile
{
    /// <summary>
    /// Runtime platform detection and device capability system.
    /// Detects iOS/Android, device tier, GPU, and applies quality scaling accordingly.
    /// </summary>
    public class PlatformDetector : MonoBehaviour
    {
        public static PlatformDetector Instance { get; private set; }

        public enum DeviceTier { LowEnd, MidRange, HighEnd }

        [System.Serializable]
        public struct DeviceProfile
        {
            public RuntimePlatform Platform;
            public DeviceTier Tier;
            public int RAM_MB;
            public string GPU;
            public float RecommendedFPS;
        }

        public DeviceProfile CurrentDevice { get; private set; }

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }

            Instance = this;
            DontDestroyOnLoad(gameObject);

            CurrentDevice = ProfileCurrentDevice();
            ApplyQualitySettings();
        }

        /// <summary>
        /// Profile current device and determine tier.
        /// </summary>
        public DeviceProfile ProfileCurrentDevice()
        {
            string gpu = SystemInfo.graphicsDeviceName;
            int ram = SystemInfo.systemMemorySize;

            DeviceTier tier = ClassifyDeviceTier(gpu, ram);

            Debug.Log($"[Platform] Detected: {Application.platform} | GPU: {gpu} | RAM: {ram}MB | Tier: {tier}");

            return new DeviceProfile
            {
                Platform = Application.platform,
                Tier = tier,
                RAM_MB = ram,
                GPU = gpu,
                RecommendedFPS = GetTargetFPS(tier)
            };
        }

        /// <summary>
        /// Classify device into tier (Low/Mid/High-End).
        /// </summary>
        private DeviceTier ClassifyDeviceTier(string gpu, int ram)
        {
            // High-End
            if (ram >= 8000 &&
                (gpu.Contains("RTX") || gpu.Contains("A16") || gpu.Contains("A17") ||
                 gpu.Contains("Snapdragon 8 Gen") || gpu.Contains("Exynos 2200")))
            {
                return DeviceTier.HighEnd;
            }

            // Low-End
            if (ram <= 3000 ||
                gpu.Contains("Adreno 505") || gpu.Contains("Snapdragon 600") ||
                gpu.Contains("Mali-400") || gpu.Contains("A9"))
            {
                return DeviceTier.LowEnd;
            }

            // Mid-Range
            return DeviceTier.MidRange;
        }

        /// <summary>
        /// Get target FPS based on device tier.
        /// </summary>
        public float GetTargetFPS(DeviceTier tier)
        {
            return tier switch
            {
                DeviceTier.HighEnd => 120f,
                DeviceTier.MidRange => 60f,
                DeviceTier.LowEnd => 30f,
                _ => 60f
            };
        }

        /// <summary>
        /// Apply quality settings based on device tier.
        /// </summary>
        public void ApplyQualitySettings()
        {
            switch (CurrentDevice.Tier)
            {
                case DeviceTier.HighEnd:
                    QualitySettings.masterTextureLimit = 0;
                    QualitySettings.anisotropicFiltering = AnisotropicFiltering.ForceEnable;
                    QualitySettings.shadowCascades = 4;
                    break;

                case DeviceTier.MidRange:
                    QualitySettings.masterTextureLimit = 0;
                    QualitySettings.anisotropicFiltering = AnisotropicFiltering.Trilinear;
                    QualitySettings.shadowCascades = 2;
                    break;

                case DeviceTier.LowEnd:
                    QualitySettings.masterTextureLimit = 1; // Half resolution
                    QualitySettings.anisotropicFiltering = AnisotropicFiltering.Disable;
                    QualitySettings.shadowCascades = 0; // No shadows
                    break;
            }

            Application.targetFrameRate = (int)GetTargetFPS(CurrentDevice.Tier);
            Debug.Log($"[Platform] Applied quality: {CurrentDevice.Tier} | Target FPS: {Application.targetFrameRate}");
        }

        /// <summary>
        /// Check if running on iOS.
        /// </summary>
        public bool IsIOS() => Application.platform == RuntimePlatform.IPhonePlayer;

        /// <summary>
        /// Check if running on Android.
        /// </summary>
        public bool IsAndroid() => Application.platform == RuntimePlatform.Android;

        /// <summary>
        /// Check if running on mobile (iOS or Android).
        /// </summary>
        public bool IsMobile() => IsIOS() || IsAndroid();

        /// <summary>
        /// Get safe area (handles notches, safe zone, etc).
        /// </summary>
        public Rect GetSafeArea()
        {
            return Screen.safeArea;
        }

        /// <summary>
        /// Check if device supports haptic feedback.
        /// </summary>
        public bool SupportsHaptics()
        {
            return IsMobile() && Handheld.IsSupported;
        }

        /// <summary>
        /// Trigger device haptic feedback.
        /// </summary>
        public void TriggerHaptic()
        {
            if (SupportsHaptics())
            {
                Handheld.Vibrate();
            }
        }

        /// <summary>
        /// Get available input methods.
        /// </summary>
        public List<string> GetAvailableInputMethods()
        {
            var methods = new List<string> { "keyboard", "mouse" };

            if (Input.touchSupported)
                methods.Add("touch");

            if (Input.gyroSupported)
                methods.Add("gyro");

            return methods;
        }

        /// <summary>
        /// Check if device in Low Power Mode (battery saver).
        /// </summary>
        public bool IsLowPowerMode()
        {
            #if UNITY_IOS
            return iOS.Device.lowPowerModeEnabled;
            #elif UNITY_ANDROID
            // Requires plugin or API call
            return false;
            #endif
        }

        /// <summary>
        /// Monitor and log device thermal state.
        /// </summary>
        public void LogThermalState()
        {
            #if UNITY_ANDROID
            var thermalStatus = SystemInfo.batteryStatus;
            Debug.Log($"[Platform] Battery: {SystemInfo.batteryLevel:P} | Status: {thermalStatus}");
            #endif
        }

        /// <summary>
        /// Get network connectivity info.
        /// </summary>
        public NetworkReachability GetNetworkStatus()
        {
            return Application.internetReachability;
        }

        public bool HasInternetConnection()
        {
            return Application.internetReachability != NetworkReachability.NotReachable;
        }
    }
}
