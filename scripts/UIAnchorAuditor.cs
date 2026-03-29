using UnityEngine;
using UnityEditor;

namespace Antigravity.UI
{
#if UNITY_EDITOR
    /// <summary>
    /// Editor tool to automatically fix UI anchors to corners.
    /// MCP can execute this to clean up messy UI layouts.
    /// </summary>
    public static class UIAnchorAuditor
    {
        [MenuItem("Antigravity/UI/Anchors To Corners")]
        public static void AnchorsToCorners()
        {
            foreach (GameObject go in Selection.gameObjects)
            {
                RectTransform t = go.GetComponent<RectTransform>();
                if (t == null) continue;

                RectTransform pt = t.parent as RectTransform;
                if (pt == null) continue;

                Undo.RecordObject(t, "Anchors to Corners");

                Vector2 offsetMin = t.offsetMin;
                Vector2 offsetMax = t.offsetMax;
                Vector2 _anchorMin = t.anchorMin;
                Vector2 _anchorMax = t.anchorMax;

                float parentWidth = pt.rect.width;
                float parentHeight = pt.rect.height;

                Vector2 anchorMin = new Vector2(_anchorMin.x + (offsetMin.x / parentWidth),
                                                _anchorMin.y + (offsetMin.y / parentHeight));
                Vector2 anchorMax = new Vector2(_anchorMax.x + (offsetMax.x / parentWidth),
                                                _anchorMax.y + (offsetMax.y / parentHeight));

                t.anchorMin = anchorMin;
                t.anchorMax = anchorMax;
                t.offsetMin = Vector2.zero;
                t.offsetMax = Vector2.zero;
            }
        }
    }
#endif
}
