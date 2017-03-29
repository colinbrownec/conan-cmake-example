import os
from conans import ConanFile, CMake

class Child(ConanFile):
  name = 'Child'
  version = '1.0'
  generators = 'cmake'
  settings = ('os', 'arch', 'compiler', 'build_type')

  options = {
    'shared': [True, False]
  }

  default_options = (
    'shared=True'
  )

  exports_sources = 'src/*', 'CMakeLists.txt'

  def build(self):
    cmake = CMake(self.settings)
    args = ' '.join([
      '-DCMAKE_INSTALL_PREFIX=%s' % self.package_folder,
      '-DBUILD_SHARED_LIBS=%s' % ('ON' if self.options.shared else 'OFF')
    ])

    self.run('cmake %s %s %s' % (self.conanfile_directory, cmake.command_line, args))
    self.run('cmake --build . --target install %s' % cmake.build_config)

  def package_info(self):
    self.cpp_info.libs = ['child']
