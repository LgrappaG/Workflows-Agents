using UnityEngine;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Antigravity.Performance
{
    /// <summary>
    /// Analyzes build size distribution across assets, code, and resources.
    /// Identifies optimization opportunities and provides compression recommendations.
    /// </summary>
    public class BuildSizeAnalyzer : MonoBehaviour
    {
        [System.Serializable]
        public struct AssetSizeReport
        {
            public string AssetPath;
            public long SizeBytes;
            public string AssetType;
            public float SizeMB => SizeBytes / (1024f * 1024f);
        }

        [System.Serializable]
        public struct BuildReport
        {
            public long TotalSizeBytes;
            public List<AssetSizeReport> LargestAssets;
            public Dictionary<string, long> SizeByType;
        }

        /// <summary>
        /// Analyze all scene assets for size distribution.
        /// </summary>
        public static BuildReport AnalyzeSceneAssets()
        {
            var report = new BuildReport
            {
                LargestAssets = new(),
                SizeByType = new()
            };

            var allAssets = Resources.FindObjectsOfTypeAll<Object>();

            foreach (var asset in allAssets)
            {
                if (asset == null || string.IsNullOrEmpty(asset.name)) continue;

                long size = EstimateAssetSize(asset);
                string assetPath = AssetDatabase.GetAssetPath(asset);
                string assetType = asset.GetType().Name;

                report.TotalSizeBytes += size;

                if (!report.SizeByType.ContainsKey(assetType))
                    report.SizeByType[assetType] = 0;

                report.SizeByType[assetType] += size;

                report.LargestAssets.Add(new AssetSizeReport
                {
                    AssetPath = assetPath,
                    SizeBytes = size,
                    AssetType = assetType
                });
            }

            report.LargestAssets = report.LargestAssets
                .OrderByDescending(a => a.SizeBytes)
                .Take(50)
                .ToList();

            PrintReport(report);
            return report;
        }

        /// <summary>
        /// Get texture memory footprint.
        /// </summary>
        public static long GetTextureMemoryUsage()
        {
            long totalMemory = 0;
            var textures = Resources.FindObjectsOfTypeAll<Texture2D>();

            foreach (var tex in textures)
            {
                if (tex == null) continue;
                totalMemory += tex.width * tex.height * GetBytesPerPixel(tex.format);
            }

            return totalMemory;
        }

        /// <summary>
        /// Get mesh memory footprint.
        /// </summary>
        public static long GetMeshMemoryUsage()
        {
            long totalMemory = 0;
            var meshes = Resources.FindObjectsOfTypeAll<Mesh>();

            foreach (var mesh in meshes)
            {
                if (mesh == null) continue;
                int vertexCount = mesh.vertexCount;
                int triangleCount = mesh.triangles.Length / 3;

                // Rough estimate: ~12 bytes per vertex + ~2 bytes per triangle
                totalMemory += (vertexCount * 12) + (triangleCount * 2);
            }

            return totalMemory;
        }

        /// <summary>
        /// Get audio memory footprint.
        /// </summary>
        public static long GetAudioMemoryUsage()
        {
            long totalMemory = 0;
            var clips = Resources.FindObjectsOfTypeAll<AudioClip>();

            foreach (var clip in clips)
            {
                if (clip == null) continue;
                // PCM: samples * channels * bytes per sample (2 bytes for 16-bit)
                totalMemory += clip.samples * clip.channels * 2;
            }

            return totalMemory;
        }

        /// <summary>
        /// Estimate total VRAM usage.
        /// </summary>
        public static (long TextureMB, long MeshMB, long AudioMB, long TotalMB) EstimateVRAMUsage()
        {
            long textureMemory = GetTextureMemoryUsage();
            long meshMemory = GetMeshMemoryUsage();
            long audioMemory = GetAudioMemoryUsage();
            long totalMemory = textureMemory + meshMemory + audioMemory;

            return (
                textureMemory / (1024 * 1024),
                meshMemory / (1024 * 1024),
                audioMemory / (1024 * 1024),
                totalMemory / (1024 * 1024)
            );
        }

        /// <summary>
        /// Get compression recommendations based on build size.
        /// </summary>
        public static List<string> GetOptimizationRecommendations(BuildReport report)
        {
            var recommendations = new List<string>();

            if (report.TotalSizeBytes > 150 * 1024 * 1024) // >150MB
            {
                recommendations.Add("❌ Build size >150MB. Enable texture compression (Crunch recommended)");
                recommendations.Add("❌ Strip unused code: Player Settings → Managed Stripping: High");
            }

            if (report.SizeByType.ContainsKey("Texture2D"))
            {
                long texSize = report.SizeByType["Texture2D"];
                if (texSize > report.TotalSizeBytes * 0.6f) // >60% textures
                {
                    recommendations.Add("⚠️ Textures dominate build (>60%). Reduce resolution or use atlasing");
                }
            }

            if (report.SizeByType.ContainsKey("AudioClip"))
            {
                long audioSize = report.SizeByType["AudioClip"];
                if (audioSize > report.TotalSizeBytes * 0.2f) // >20% audio
                {
                    recommendations.Add("⚠️ Audio is large (>20%). Use Vorbis compression, stream long clips");
                }
            }

            recommendations.Add("✅ Use Addressables for on-demand loading");
            recommendations.Add("✅ Implement asset bundles for modular distribution");

            return recommendations;
        }

        private static long EstimateAssetSize(Object asset)
        {
            if (asset is Texture2D tex)
                return tex.width * tex.height * GetBytesPerPixel(tex.format);

            if (asset is Mesh mesh)
                return mesh.vertexCount * 12; // Rough estimate

            if (asset is AudioClip audio)
                return audio.samples * audio.channels * 2;

            return 0;
        }

        private static int GetBytesPerPixel(TextureFormat format)
        {
            return format switch
            {
                TextureFormat.RGBA32 => 4,
                TextureFormat.RGB24 => 3,
                TextureFormat.ARGB32 => 4,
                TextureFormat.DXT1 => 1, // ~0.5 bytes per pixel
                TextureFormat.DXT5 => 1, // ~1 byte per pixel
                TextureFormat.ASTC_6x6 => 1,
                TextureFormat.ETC2_RGB => 1,
                _ => 4
            };
        }

        private static void PrintReport(BuildReport report)
        {
            Debug.Log($"=== BUILD SIZE REPORT ===");
            Debug.Log($"Total Size: {report.TotalSizeBytes / (1024f * 1024f):F2} MB");
            Debug.Log($"\nTop 10 Largest Assets:");

            for (int i = 0; i < Mathf.Min(10, report.LargestAssets.Count); i++)
            {
                var asset = report.LargestAssets[i];
                Debug.Log($"{i + 1}. {asset.AssetPath} ({asset.SizeMB:F2}MB) [{asset.AssetType}]");
            }

            Debug.Log($"\nSize by Type:");
            foreach (var type in report.SizeByType.OrderByDescending(x => x.Value))
            {
                Debug.Log($"  {type.Key}: {type.Value / (1024f * 1024f):F2}MB");
            }

            Debug.Log($"\nRecommendations:");
            foreach (var rec in GetOptimizationRecommendations(report))
            {
                Debug.Log(rec);
            }
        }
    }
}
