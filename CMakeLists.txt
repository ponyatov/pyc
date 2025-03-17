    cmake_minimum_required(VERSION 3.22)
    get_filename_component(CMAKE_PROJECT_NAME ${CMAKE_SOURCE_DIR} NAME_WE)
    project(${CMAKE_PROJECT_NAME} LANGUAGES C CXX ASM)
include_directories(${INC})

file(GLOB C
)

file(GLOB H
)

file(GLOB INC
)

    message("-- |")
    message("-- | app: " ${CMAKE_PROJECT_NAME})
    message("-- |")

add_executable(${CMAKE_PROJECT_NAME}
    ${C}  ${H}  # C/C++ source
)

install(TARGETS ${CMAKE_PROJECT_NAME}
    DESTINATION ${CMAKE_INSTALL_PREFIX})
