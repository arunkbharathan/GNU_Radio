INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TUTORIAL_CPP tutorial_cpp)

FIND_PATH(
    TUTORIAL_CPP_INCLUDE_DIRS
    NAMES tutorial_cpp/api.h
    HINTS $ENV{TUTORIAL_CPP_DIR}/include
        ${PC_TUTORIAL_CPP_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TUTORIAL_CPP_LIBRARIES
    NAMES gnuradio-tutorial_cpp
    HINTS $ENV{TUTORIAL_CPP_DIR}/lib
        ${PC_TUTORIAL_CPP_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TUTORIAL_CPP DEFAULT_MSG TUTORIAL_CPP_LIBRARIES TUTORIAL_CPP_INCLUDE_DIRS)
MARK_AS_ADVANCED(TUTORIAL_CPP_LIBRARIES TUTORIAL_CPP_INCLUDE_DIRS)

