using UnityEngine;
using System.Collections.Generic;

/// <summary>
/// Marks game objects with skill metadata for validation and showcase purposes.
/// Enables automation of skill→component binding for DemoManifest.json generation.
/// </summary>
[System.Serializable]
public class SkillBindingInfo
{
    public string skillId;
    public string skillCategory;
    public string usage;
    public int validationGate;
}

public class SkillShowcaseMarker : MonoBehaviour
{
    [SerializeField] public List<SkillBindingInfo> activeSkills = new List<SkillBindingInfo>();

    [TextArea(3, 5)]
    [SerializeField] public string componentNote = "";

    /// <summary>
    /// Extract all skill markers from the scene and return as serializable data.
    /// </summary>
    public static List<SkillShowcaseMarker> FindAllMarkers(GameObject rootObject)
    {
        return new List<SkillShowcaseMarker>(rootObject.GetComponentsInChildren<SkillShowcaseMarker>());
    }

    /// <summary>
    /// Register a skill for this component.
    /// </summary>
    public void RegisterSkill(string skillId, string category, string usage, int gate)
    {
        if (!activeSkills.Exists(s => s.skillId == skillId))
        {
            activeSkills.Add(new SkillBindingInfo
            {
                skillId = skillId,
                skillCategory = category,
                usage = usage,
                validationGate = gate
            });
        }
    }

    public void OnValidate()
    {
        // Cleanup duplicates during edit time
        var uniqueSkills = new Dictionary<string, SkillBindingInfo>();
        foreach (var skill in activeSkills)
        {
            uniqueSkills[skill.skillId] = skill;
        }
        activeSkills = new List<SkillBindingInfo>(uniqueSkills.Values);
    }
}
