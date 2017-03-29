project(child CXX)

if (WIN32)
  cmake_minimum_required(VERSION 3.4)
  set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)
else()
  cmake_minimum_required(VERSION 2.8)
endif()

add_library(child src/child.cpp)

install(
  DIRECTORY src/
  DESTINATION include
  FILES_MATCHING PATTERN "*.h"
)

install(
  TARGETS child
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin
)
