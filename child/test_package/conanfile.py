from conans import ConanFile, CMake
import os

class ChildTestProject(ConanFile):
  settings = ('os', 'arch', 'compiler', 'build_type')
  requires = 'Child/1.0@example/stable'
  generators = 'cmake'

  def build(self):
    cmake = CMake(self.settings)

    self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
    self.run('cmake --build . %s' % cmake.build_config)

  def imports(self):
    self.copy(pattern='*.dll', src='bin', dst='bin')

  def test(self):
    # equal to ./bin/child_test_project, but portable on windows
    self.run(os.sep.join(['.', 'bin', 'child_test_project']))
