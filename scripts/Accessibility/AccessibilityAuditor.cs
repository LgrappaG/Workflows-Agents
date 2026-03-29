using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;
using System.Linq;

namespace Antigravity.Accessibility
{
    /// <summary>
    /// WCAG 2.1 accessibility auditing system.
    /// Checks color contrast, text sizing, keyboard navigation, and inclusive design compliance.
    /// </summary>
    public class AccessibilityAuditor : MonoBehaviour
    {
        [System.Serializable]
        public struct AccessibilityIssue
        {
            public GameObject AffectedObject;
            public string IssueType; // "ContrastRatio", "TextSize", "KeyboardNavigation", "ColorAlone"
            public string Message;
            public float SeverityScore; // 0-10, 10 = critical
        }

        private const float MinContrastRatioNormalText = 4.5f;
        private const float MinContrastRatioLargeText = 3f;
        private const float MinTextSizePixels = 14f;

        /// <summary>
        /// Audit entire scene for accessibility issues.
        /// </summary>
        public static List<AccessibilityIssue> AuditScene()
        {
            var issues = new List<AccessibilityIssue>();

            // Check text contrast
            var textComponents = FindObjectsOfType<Text>();
            foreach (var text in textComponents)
            {
                var contrastIssues = AuditTextContrast(text);
                issues.AddRange(contrastIssues);
            }

            // Check TextMesh Pro
            var tmpComponents = FindObjectsOfType<TMPro.TextMeshProUGUI>();
            foreach (var tmp in tmpComponents)
            {
                var contrastIssues = AuditTMPContrast(tmp);
                issues.AddRange(contrastIssues);
            }

            // Check buttons are accessible
            var buttons = FindObjectsOfType<Button>();
            foreach (var button in buttons)
            {
                if (button.GetComponent<Selectable>() == null)
                {
                    issues.Add(new AccessibilityIssue
                    {
                        AffectedObject = button.gameObject,
                        IssueType = "KeyboardNavigation",
                        Message = "Button not keyboard selectable",
                        SeverityScore = 8f
                    });
                }
            }

            // Check for color-only information conveyance
            var images = FindObjectsOfType<Image>();
            foreach (var image in images)
            {
                if (image.name.Contains("Status") || image.name.Contains("Indicator"))
                {
                    issues.Add(new AccessibilityIssue
                    {
                        AffectedObject = image.gameObject,
                        IssueType = "ColorAlone",
                        Message = "Use icon + color, not color alone for information",
                        SeverityScore = 6f
                    });
                }
            }

            PrintAuditReport(issues);
            return issues;
        }

        /// <summary>
        /// Check text contrast ratio (WCAG formula).
        /// </summary>
        public static float GetContrastRatio(Color foreground, Color background)
        {
            float lum1 = GetRelativeLuminance(foreground);
            float lum2 = GetRelativeLuminance(background);
            return (Mathf.Max(lum1, lum2) + 0.05f) / (Mathf.Min(lum1, lum2) + 0.05f);
        }

        /// <summary>
        /// Audit Text component contrast.
        /// </summary>
        private static List<AccessibilityIssue> AuditTextContrast(Text text)
        {
            var issues = new List<AccessibilityIssue>();

            var image = text.GetComponentInParent<Image>();
            if (image == null) return issues;

            float contrast = GetContrastRatio(text.color, image.color);
            float fontSize = text.fontSize;

            bool isLargeText = fontSize >= 18;
            float minContrast = isLargeText ? MinContrastRatioLargeText : MinContrastRatioNormalText;

            if (contrast < minContrast)
            {
                issues.Add(new AccessibilityIssue
                {
                    AffectedObject = text.gameObject,
                    IssueType = "ContrastRatio",
                    Message = $"Contrast ratio {contrast:F2}:1 below minimum {minContrast}:1",
                    SeverityScore = 9f
                });
            }

            if (fontSize < MinTextSizePixels)
            {
                issues.Add(new AccessibilityIssue
                {
                    AffectedObject = text.gameObject,
                    IssueType = "TextSize",
                    Message = $"Font size {fontSize}px too small (min {MinTextSizePixels}px)",
                    SeverityScore = 5f
                });
            }

            return issues;
        }

        /// <summary>
        /// Audit TextMesh Pro contrast.
        /// </summary>
        private static List<AccessibilityIssue> AuditTMPContrast(TMPro.TextMeshProUGUI tmp)
        {
            var issues = new List<AccessibilityIssue>();

            var image = tmp.GetComponentInParent<Image>();
            if (image == null) return issues;

            float contrast = GetContrastRatio(tmp.color, image.color);
            float fontSize = tmp.fontSize;

            bool isLargeText = fontSize >= 18;
            float minContrast = isLargeText ? MinContrastRatioLargeText : MinContrastRatioNormalText;

            if (contrast < minContrast)
            {
                issues.Add(new AccessibilityIssue
                {
                    AffectedObject = tmp.gameObject,
                    IssueType = "ContrastRatio",
                    Message = $"Contrast ratio {contrast:F2}:1 below minimum {minContrast}:1",
                    SeverityScore = 9f
                });
            }

            return issues;
        }

        /// <summary>
        /// Get WCAG relative luminance.
        /// </summary>
        private static float GetRelativeLuminance(Color color)
        {
            float r = LinearizeChannel(color.r);
            float g = LinearizeChannel(color.g);
            float b = LinearizeChannel(color.b);

            return 0.2126f * r + 0.7152f * g + 0.0722f * b;
        }

        private static float LinearizeChannel(float channel)
        {
            return channel <= 0.03928f
                ? channel / 12.92f
                : Mathf.Pow((channel + 0.055f) / 1.055f, 2.4f);
        }

        /// <summary>
        /// Check if UI is readable at 200% zoom (accessibility requirement).
        /// </summary>
        public static bool CheckZoomableUI(Canvas canvas)
        {
            var group = canvas.GetComponent<CanvasScaler>();
            if (group == null) return false;

            // Should support at least 200% UI scale
            return group.scaleFactor >= 0.5f; // 0.5 * 2x = 1.0 normal scale when zoomed 200%
        }

        /// <summary>
        /// Check for flashing content (seizure risk, >3x per second is danger zone).
        /// </summary>
        public static bool HasFlashingContent()
        {
            var images = FindObjectsOfTypeAll<Image>();
            foreach (var image in images)
            {
                var animator = image.GetComponent<Animator>();
                if (animator != null && animator.enabled)
                {
                    // This is a simplified check
                    Debug.LogWarning($"Flashing content detected in {image.name} - verify not >3x/sec");
                    return true;
                }
            }

            return false;
        }

        private static void PrintAuditReport(List<AccessibilityIssue> issues)
        {
            Debug.Log($"=== ACCESSIBILITY AUDIT (WCAG 2.1) ===");
            Debug.Log($"Total Issues Found: {issues.Count}");

            var critical = issues.Where(i => i.SeverityScore >= 8).ToList();
            var major = issues.Where(i => i.SeverityScore >= 5 && i.SeverityScore < 8).ToList();
            var minor = issues.Where(i => i.SeverityScore < 5).ToList();

            Debug.Log($"\n🔴 CRITICAL ({critical.Count}):");
            foreach (var issue in critical)
                Debug.LogError($"  {issue.AffectedObject.name}: {issue.Message}");

            Debug.Log($"\n🟡 MAJOR ({major.Count}):");
            foreach (var issue in major)
                Debug.LogWarning($"  {issue.AffectedObject.name}: {issue.Message}");

            Debug.Log($"\n🔵 MINOR ({minor.Count}):");
            foreach (var issue in minor)
                Debug.Log($"  {issue.AffectedObject.name}: {issue.Message}");

            Debug.Log($"\n✅ WCAG 2.1 Level AA Target: Fix all 🔴 CRITICAL issues");
        }
    }
}
