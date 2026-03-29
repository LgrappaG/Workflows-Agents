using UnityEngine;

namespace Antigravity.Core.Utils
{
    /// <summary>
    /// Configuration profile for standardizing the rotational and positional offsets of flawed 3D prefabs.
    /// </summary>
    [CreateAssetMenu(fileName = "NewPlacementProfile", menuName = "Antigravity Core/Utils/Placement Profile")]
    public class PlacementProfile : ScriptableObject
    {
        [Tooltip("If true, the object's lowest render bounds will be snapped to the target position.")]
        public bool snapToFloor = true;
        
        [Tooltip("Euler rotation offset applied when placing this object.")]
        public Vector3 rotationOffset = Vector3.zero;
        
        [Tooltip("Positional offset applied after snapping (useful for objects with bad pivots).")]
        public Vector3 positionOffset = Vector3.zero;

        [Tooltip("If true, the door/chest will have a hinge proxy injected at the lowest-left bound.")]
        public bool requiresHingeInjection = false;
        
        [Tooltip("Offset from the calculated bounds for the hinge (X=width, Y=height, Z=depth).")]
        public Vector3 hingeOffset = Vector3.zero;
    }
}
