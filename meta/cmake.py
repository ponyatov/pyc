from fio import *
from src import *

class CMakeLists(File):
    def __init__(self):
        super().__init__('CMakeLists.txt')
        self / (S()
                / 'cmake_minimum_required(VERSION 3.22)'
                / 'get_filename_component(CMAKE_PROJECT_NAME ${CMAKE_SOURCE_DIR} NAME_WE)'
                / 'project(${CMAKE_PROJECT_NAME} LANGUAGES C CXX ASM)')
        self / 'include_directories(${INC})'

        self / (S('\nfile(GLOB C', ')'))
        self / (S('\nfile(GLOB H', ')'))
        self / (S('\nfile(GLOB INC', ')'))
        self / (S('')
                / 'message("-- |")'
                / 'message("-- | app: " ${CMAKE_PROJECT_NAME})'
                / 'message("-- |")'
                )
        self / (S('\nadd_executable(${CMAKE_PROJECT_NAME}', ')')
                / '${C}  ${H}  # C/C++ source')
        self / (S('\ninstall(TARGETS ${CMAKE_PROJECT_NAME}')
                / 'DESTINATION ${CMAKE_INSTALL_PREFIX})')

class CMakePresets(File):
    def __init__(self):
        super().__init__('CMakePresets.json')
        self.common = S('{', '},') \
            / '"name"           : "common",' \
            / '"hidden"         :  true,' \
            / '"binaryDir"      : "${sourceDir}/tmp/${presetName}",' \
            / '"generator"      : "Unix Makefiles",' \
            / S('"cacheVariables" : {', '}')
        self.linux = S('{', '}') \
            / '"name"           : "linux",' \
            / '"inherits"       : "common",' \
            / S('"cacheVariables" : {', '}')
        self.configurePresets = S(
            '"configurePresets": [', ']') / self.common / self.linux
        self / (S('{', '}') / '"version": 6,' / self.configurePresets)

cmk = CMakeLists()
cpr = CMakePresets()
