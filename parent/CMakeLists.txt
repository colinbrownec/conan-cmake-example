project(Parent CXX)
cmake_minimum_required(VERSION 2.8)

set(LOCAL "" CACHE PATH "Include libraries from a local cache.")
if(LOCAL)
  message(STATUS "Using local cache libraries from: ${LOCAL}")
  include_directories(${LOCAL}/include)
  link_directories(${LOCAL}/lib)
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(parent src/parent.cpp)
target_link_libraries(parent child)
