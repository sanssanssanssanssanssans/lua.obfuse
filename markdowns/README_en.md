# Lua.obfuse

- Lua.obfuse is a tool that bundles a Lua project into a single compressed file (`*.o.lua`).
It registers each Lua file into an internal module registry, compresses and encodes them, and allows them to be decompressed and executed at runtime.

# Features

- Collects all .lua files starting from target/target.lua
- Rewrites require('a.b') calls into runtime calls __require('a.b')
- Registers each file in a predefined bundled format
- Generates a single output file that includes the runtime execution template

# Quick-Start

- Place your Lua project under the target/ directory (You can specify a different entry path using the --entry argument.)
- Run the bundler:
```python
python src/main.py --entry target/target.lua --output target/target.o.lua
```
- Execute the generated bundle with Lua:

# Notes

- By default, the entry file is assumed to be inside the bundle root directory. To bundle files from a different location. Change the root when creating the Packager, or Provide an appropriate path via the --entry option.
- The generated .o.lua file depends only on the packager’s runtime loader. No external Lua files or modules are required at runtime.