cmake_minimum_required(VERSION 3.17)
project(qmc_decode)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

#add_executable(test src/main.c src/qmc_crypto.c src/qmc_crypto.h)

add_library(qmc_decode SHARED src/qmc_crypto.c src/qmc_crypto.h)

link_libraries(qmc_decode)
add_executable(test src/main.c)
