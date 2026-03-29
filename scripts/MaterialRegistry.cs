using UnityEngine;
using System.Collections.Generic;

#if UNITY_EDITOR
using UnityEditor;
#endif

namespace Antigravity.Core.Utils
{
    /// <summary>
    /// Centralized registry for caching and generating URP/Standard fallback materials at runtime/editor time.
    /// Prevents duplicate material generation and missing shader pink errors.
    /// </summary>
    [CreateAssetMenu(fileName = "MaterialRegistry", menuName = "Antigravity Core/Utils/Material Registry")]
    public class MaterialRegistry : ScriptableObject
    {
        [System.Serializable]
        public class MaterialDefinition
        {
            public string id;
            public Material material;
        }

        public List<MaterialDefinition> materials = new List<MaterialDefinition>();

        private static MaterialRegistry _instance;
        public static MaterialRegistry Instance
        {
            get
            {
                if (_instance == null)
                {
#if UNITY_EDITOR
                    string[] guids = UnityEditor.AssetDatabase.FindAssets("t:MaterialRegistry");
                    if (guids.Length > 0)
                    {
                        string path = UnityEditor.AssetDatabase.GUIDToAssetPath(guids[0]);
                        _instance = UnityEditor.AssetDatabase.LoadAssetAtPath<MaterialRegistry>(path);
                    }
#endif
                }
                return _instance;
            }
        }

        public Material GetMaterial(string id)
        {
            var match = materials.Find(m => m.id == id);
            return match?.material;
        }

#if UNITY_EDITOR
        public Material GetOrCreateMaterial(string id, Color defaultColor, bool isTransparent = false)
        {
            Material mat = GetMaterial(id);
            if (mat != null) return mat;

            // Generate fallback
            if (!UnityEditor.AssetDatabase.IsValidFolder("Assets/Materials"))
                UnityEditor.AssetDatabase.CreateFolder("Assets", "Materials");

            string path = $"Assets/Materials/{id}.mat";
            mat = UnityEditor.AssetDatabase.LoadAssetAtPath<Material>(path);

            if (mat == null)
            {
                Shader shader = Shader.Find("Universal Render Pipeline/Lit");
                if (shader == null) shader = Shader.Find("Standard");

                mat = new Material(shader);
                if (shader.name.Contains("Universal Render Pipeline"))
                    mat.SetColor("_BaseColor", defaultColor);
                else
                    mat.color = defaultColor;

                if (isTransparent)
                {
                    if (shader.name.Contains("Universal Render Pipeline"))
                    {
                        mat.SetFloat("_Surface", 1); // Transparent
                        mat.SetFloat("_Blend", 0); // Alpha
                        mat.renderQueue = 3000;
                    }
                    else
                    {
                        mat.SetFloat("_Mode", 3);
                        mat.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.One);
                        mat.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.OneMinusSrcAlpha);
                        mat.SetInt("_ZWrite", 0);
                        mat.DisableKeyword("_ALPHATEST_ON");
                        mat.DisableKeyword("_ALPHABLEND_ON");
                        mat.EnableKeyword("_ALPHAPREMULTIPLY_ON");
                        mat.renderQueue = 3000;
                    }
                }

                UnityEditor.AssetDatabase.CreateAsset(mat, path);
                UnityEditor.AssetDatabase.SaveAssets();
            }

            materials.Add(new MaterialDefinition { id = id, material = mat });
            UnityEditor.EditorUtility.SetDirty(this);
            UnityEditor.AssetDatabase.SaveAssets();

            return mat;
        }
#endif
    }
}
