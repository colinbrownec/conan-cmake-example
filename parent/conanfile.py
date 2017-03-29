import os
import shutil
from conans import ConanFile, CMake

class Parent(ConanFile):
  name = 'Parent'
  version = '1.0'
  generators = 'cmake'
  settings = ('os', 'arch', 'compiler', 'build_type')

  requires = 'Child/1.0@example/stable'

  def imports(self):
    for directory in self.deps_cpp_info.bindirs:
      self.copy(pattern='*.dll', src=directory, dst='bin')
