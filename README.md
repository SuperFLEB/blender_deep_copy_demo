# Deep Copy Demo

https://github.com/SuperFLEB/blender_deep_copy_demo

This is a Blender addon that demonstrates the [Deep Copy Library](https://github.com/SuperFLEB/blender_deepcopy_lib)
and can be used for debug and development.

## Features

Adds an operator that makes in-place copies of objects and their data, materials, and the nodegroups in materials.
If there are collection instances, those are copied as well.

* All data is made unique from unselected objects, but is common among the selection.
* Some features will fail to copy or will behave unexpectedly:
  * Vertex instances
  * Geometry nodes

## To install

Before installing, be sure to initialize submodules, as this includes the library as a submodule.

Either install the ZIP file from the release, clone this repository and use the
build_release.py script to build a ZIP file that you can install into Blender.

## To use

1. Select one or more objects.
2. Press Spacebar/W (depending on mode) to open the context menu.
3. In the "Deep Copy Demo", select "Deep Copy"
4. Notice how everything's the same, but different now.

## Testing

Tests don't exist yet, but there will probably be some.

To run unit tests, run (from the Blender install directory):

```shell
blender --factory-startup --background --python path/to/module/run_tests.py
```
