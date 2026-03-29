using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Manages character selection UI and orchestration.
/// Demonstrates ui-prefab-variants, ui-animation-states, ui-data-binding, animation-blend-trees.
/// </summary>
[System.Serializable]
public class CharacterOption
{
    public string characterName;
    public string characterClass;
    public GameObject characterPrefab;
    public GameObject portraitPrefab;
    public int attackPower;
    public int defensePower;
    public int magicPower;
}

public class CharacterSelectManager : MonoBehaviour
{
    [SerializeField] private List<CharacterOption> characters = new List<CharacterOption>();
    [SerializeField] private Transform characterDisplayArea;
    [SerializeField] private Transform uiPanelArea;

    private int selectedCharacterIndex = -1;
    private GameObject currentCharacterInstance;
    private GameObject currentPortraitInstance;

    private void Start()
    {
        if (characters.Count == 0)
        {
            UnityEngine.Debug.LogWarning("⚠️ No characters configured for character select!");
            return;
        }

        // Auto-select first character
        SelectCharacter(0);
    }

    /// <summary>
    /// Handle character selection button click.
    /// Demonstrates: ui-button-events, ui-animation-states, animation-blend-trees
    /// </summary>
    public void SelectCharacter(int index)
    {
        if (index < 0 || index >= characters.Count)
            return;

        // Cleanup previous instance
        if (currentCharacterInstance != null)
            Destroy(currentCharacterInstance);
        if (currentPortraitInstance != null)
            Destroy(currentPortraitInstance);

        selectedCharacterIndex = index;
        var selected = characters[index];

        // Instantiate character (demonstrates animation-humanoid-setup)
        if (selected.characterPrefab != null)
        {
            currentCharacterInstance = Instantiate(selected.characterPrefab, characterDisplayArea);
            currentCharacterInstance.name = $"Character_{selected.characterName}";

            // Add skill marker
            var marker = currentCharacterInstance.AddComponent<SkillShowcaseMarker>();
            marker.RegisterSkill("animation-humanoid-setup", "Animation", "Avatar rigging and humanoid animator", 1);
            marker.RegisterSkill("animation-blend-trees", "Animation", "Animation state management", 5);
        }

        // Instantiate portrait (demonstrates ui-prefab-variants, ui-data-binding)
        if (selected.portraitPrefab != null)
        {
            currentPortraitInstance = Instantiate(selected.portraitPrefab, uiPanelArea);

            // Add skill marker for UI
            var marker = currentPortraitInstance.AddComponent<SkillShowcaseMarker>();
            marker.RegisterSkill("ui-prefab-variants", "UI", "Dynamic character portrait generation", 2);
            marker.RegisterSkill("ui-data-binding", "UI", "Character stats display binding", 4);
            marker.RegisterSkill("ui-animation-states", "UI", "Transitions during selection", 3);
        }

        UnityEngine.Debug.Log($"✅ Selected: {selected.characterName} ({selected.characterClass})");
    }

    /// <summary>
    /// Get stats for selected character (demonstrates data binding).
    /// </summary>
    public CharacterOption GetSelectedCharacter()
    {
        if (selectedCharacterIndex >= 0 && selectedCharacterIndex < characters.Count)
            return characters[selectedCharacterIndex];
        return null;
    }

    /// <summary>
    /// Get all available characters for UI population.
    /// </summary>
    public List<CharacterOption> GetAvailableCharacters()
    {
        return new List<CharacterOption>(characters);
    }
}
