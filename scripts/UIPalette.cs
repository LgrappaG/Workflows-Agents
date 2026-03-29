using UnityEngine;
using TMPro;

namespace Antigravity.UI
{
    [CreateAssetMenu(fileName = "NewUIPalette", menuName = "Antigravity/UI/Vibe Palette")]
    public class UIPalette : ScriptableObject
    {
        public string themeName = "Apocalypse";

        [Header("Sprites")]
        public Sprite buttonSprite;
        public Sprite panelSprite;
        public Sprite progressBackSprite;
        public Sprite progressFillSprite;

        [Header("Fonts & Colors")]
        public TMP_FontAsset mainFont;
        public Color primaryColor = Color.white;
        public Color accentColor = Color.red;
        public Color backgroundColor = new Color(0.1f, 0.1f, 0.1f, 0.9f);
    }
}
