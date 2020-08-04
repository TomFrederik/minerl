"""Handlers relating to world generation."""

import jinja2
from minerl.herobraine.hero.handler import Handler


class DefaultWorldGenerator(Handler):
    def to_string(self) -> str:
        return "default_world_generator"

    
    def xml_template(self) -> jinja2.Template:
        return jinja2.Template(
            """<DefaultWorldGenerator 
                forceReset="{{str(force_reset).lower()}}"
                generatorOptions='{{generator_options}}'/>
            """
        )

    def __init__(self, force_reset=True, generator_options : str = "{}"):
        """Generates a world using minecraft procedural generation.

        Args:
            force_reset (bool, optional): If the world should be reset every episode.. Defaults to True.
            generator_options: A JSON object specifying parameters to the procedural generator.
        """
        self.force_reset = force_reset
        generator_options = generator_options.replace('"', "'")
        self.generator_options = generator_options
        
class FileWorldGenerator(Handler):
    """Generates a world from a file."""
    def to_string(self) -> str:
        return "file_world_generator"

    def xml_template(self) -> jinja2.Template:
        return jinja2.Template(
            """<FileWorldGenerator 
                destroyAfterUse = "{{str(destroy_after_use).lower()}}"
                src = "{{filename}}" />
            """
        )
        
    def __init__(self, filename: str, destroy_after_use : bool =True):

        self.filename = filename
        self.destroy_after_use = destroy_after_use


#  <FlatWorldGenerator forceReset="true"/>
class FlatWorldGenerator(Handler):
    """Generates a world that is a flat landscape."""
    def to_string(self) -> str:
        return "flat_world_generator"

    def xml_template(self) -> jinja2.Template:
        return jinja2.Template(
            """<FlatWorldGenerator 
                forceReset="{{str(force_reset).lower()}}" />
            """
        )
    
    def __init__(self, force_reset: bool =True):
        self.force_reset = force_reset

#  <BiomeGenerator forceReset="true" biome="3"/>
class BiomeGenerator(Handler):    
    def to_string(self) -> str:
        return "biome_generator"
    
    def xml_template(self) -> jinja2.Template:
        return jinja2.Template(
            """<BiomeGenerator 
                forceReset="{{str(force_reset).lower()}}"
                biome="{{biome_id}}" />
            """
        )
        
    def __init__(self,  biome_id: int, force_reset: bool =True):
        self.biome_id = biome_id
        self.force_reset = force_reset
