#include "qmc_crypto.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>


int main(int argc, char** argv)
{
	printf("QMC decoder (cli) v1.0 by Jixun\n");
	printf("\n");

	// check arguments
	if (argc < 3)
	{
		printf("usage: %s <input> <output> [ignored]\n", argv[0]);
		return 1;
	}

    int res;
	res = encode_decode(argv[1], argv[2]);
	return res;
}
