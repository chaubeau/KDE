project(T3)
cmake_minimum_required(VERSION 2.6)
find_package(Qt4 REQUIRED)

include_directories(${QT_INCLUDES} ${CMAKE_CURRENT_BINARY_DIR})

set(T3_SRCS T3.cpp main.cpp)
qt4_automoc(${T3_SRCS})
add_executable(T3 ${T3_SRCS})
target_link_libraries(T3 ${QT_QTCORE_LIBRARY} ${QT_QTGUI_LIBRARY})
install(TARGETS T3 RUNTIME DESTINATION bin)
