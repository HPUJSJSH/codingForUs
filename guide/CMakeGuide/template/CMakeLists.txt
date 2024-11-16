cmake_minimum_required(VERSION 3.0)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/build/bin)
set(LIBRARY_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/build/lib)
# message(STATIC ${CMAKE_CURRENT_SOURCE_DIR})
PROJECT(main)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src SRC_LIST)

add_executable(${PROJECT_NAME} ${SRC_LIST})
