from .loader import load_from_data_url

class SingleImageDataUrlLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "data_url": ("STRING", { "default": "" }),
                    },
                }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load"
    CATEGORY = "Tools"
    def load(self, data_url):
        return (load_from_data_url(data_url),)


NODE_CLASS_MAPPINGS = {
    "SingleImageDataUrlLoader": SingleImageDataUrlLoader,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SingleImageDataUrlLoader": "SingleImageDataUrlLoader",
}
