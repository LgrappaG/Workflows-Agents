namespace Antigravity.Core.Interaction
{
    /// <summary>
    /// Implemented by any object the player can interact with (Doors, Light switches, Cabinets, Loot).
    /// </summary>
    public interface IInteractable
    {
        /// <summary>
        /// Logic executed when the player presses the interact key.
        /// </summary>
        void Interact();

        /// <summary>
        /// The instruction text shown to the player when looking at the object.
        /// e.g. "Press [E] to Open Door"
        /// </summary>
        /// <returns>Formatted prompt string.</returns>
        string GetPrompt();
    }
}
