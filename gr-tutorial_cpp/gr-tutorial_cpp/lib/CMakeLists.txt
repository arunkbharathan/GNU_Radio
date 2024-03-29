# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND tutorial_cpp_sources
    my_qpsk_demod_cb_impl.cc
)

set(tutorial_cpp_sources "${tutorial_cpp_sources}" PARENT_SCOPE)
if(NOT tutorial_cpp_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT tutorial_cpp_sources)

add_library(gnuradio-tutorial_cpp SHARED ${tutorial_cpp_sources})
target_link_libraries(gnuradio-tutorial_cpp ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-tutorial_cpp PROPERTIES DEFINE_SYMBOL "gnuradio_tutorial_cpp_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-tutorial_cpp PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-tutorial_cpp
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_tutorial_cpp_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_tutorial_cpp.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_tutorial_cpp.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_my_qpsk_demod_cb.cc
)

add_executable(test-tutorial_cpp ${test_tutorial_cpp_sources})

target_link_libraries(
  test-tutorial_cpp
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-tutorial_cpp
)

GR_ADD_TEST(test_tutorial_cpp test-tutorial_cpp)
