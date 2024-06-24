import os
import numpy as np
import torch
from PIL import Image

class ChessPiecePrompt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "piece": (["King", "Queen", "Bishop", "Knight", "Rook", "Pawn"],),
                "color": (["white", "black"],)
            }
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("prompt", "image")

    FUNCTION = "generate_prompt"

    CATEGORY = "Chess"

    def load_image(self, image_path):
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            image_array = np.array(img).astype(np.float32) / 255.0
            # Convert the numpy array to a PyTorch tensor and adjust dimensions
            image_tensor = torch.tensor(image_array).permute(2, 0, 1).unsqueeze(0)
            return image_tensor

    def generate_prompt(self, piece, color):
        prompt_map = {
            "King": "(solo) chess piece (realistic:2), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.7), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a king, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (holding a sword:1.3)",
            "Queen": "(solo) chess piece (realistic:2), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.7), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a queen, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Rook": "(solo) chess piece (realistic:2), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.7), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a rook, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Bishop": "(solo) chess piece (realistic:2), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.7), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a bishop, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Knight": "(solo) chess piece (realistic:2), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.5), (polished:0.9), (intricate engravings:1.1), maintaining the shape and features of a knight, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (riding a horse:1.3)",
            "Pawn": "(solo) chess piece (realistic:2), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.7), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a pawn, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }

        image_folder = "whiteImages" if color == "white" else "blackImages"
        image_path = os.path.join(os.path.dirname(__file__), image_folder, f"{piece.lower()}.png")
        image_tensor = self.load_image(image_path)
        return (prompt_map[piece], image_tensor)

NODE_CLASS_MAPPINGS = {
    "ChessPiecePrompt": ChessPiecePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePrompt": "Chess Piece Prompt"
}