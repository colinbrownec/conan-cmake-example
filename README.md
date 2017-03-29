This is an example of two Conan based C++ projects named parent and child,
where parent has a dependency on child.

There are two workflows that are outlined below.

## 1. Production
This workflow is meant to build a new parent project entirely from source.

export child
``` cmd
cd child
conan export example/stable
```

build parent (invoking child build)
``` cmd
cd parent
mkdir build && cd build

conan install .. --build child
cmake -G "Visual Studio 12 2013 Win64" ..
cmake --build . --config release
```

## 2. Development
This workflow allows development on both the parent and child project.

To accomplish this we export an environment variable to refer to the local cache
location. It's worth nothing that this location is entirely outside the realm
of Conan.
``` cmd
set LOCAL=C:\local12md
```

install child to local cache
``` cmd
cd child
mkdir build && cd build

cmake -G "Visual Studio 12 2013 Win64" -DCMAKE_INSTALL_PREFIX=%LOCAL% -DBUILD_SHARED_LIBS=OFF ..
cmake --build . --config release --target install
```

build parent
``` cmd
cd parent
mkdir build && cd build

conan install .. --build child
cmake -G "Visual Studio 12 2013 Win64" -DLOCAL=%LOCAL% ..
cmake --build . --config release
```

### Notes
There are several problems with the current approach for a development workflow.

1. Requires child to be built statically (no way to update shared objects)
2. Stuck with package details (like defines and linker options) from the original `conan install`
