#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <packed_input_path> <unpacked_output_path>\n", argv[0]);
        return 1;
    }

    const char *input_path = argv[1];
    const char *output_path = argv[2];

    uint16_t *input_data;
    long input_size;

    {
        FILE *stream;

        stream = fopen(input_path, "rb");

        fseek(stream, 0L, SEEK_END);
        input_size = ftell(stream);
        fseek(stream, 0L, SEEK_SET);

        input_data = (uint16_t *) malloc(input_size);
        fread(input_data, 2, input_size / 2, stream);

        fclose(stream);
    }

    long n_pixels = (input_size/2);

    printf(" Pixel count: %ld\n", n_pixels);


    uint16_t *output_buffer = (uint16_t *) calloc(n_pixels * 14 / 8, 2);//n_pixels

    for (int i = 0; i < n_pixels; i++) {
        long word_offset = i * 14 / 16;
        long bit_offset = i * 14 % 16;

        if (bit_offset <= 2) {
            output_buffer[word_offset] |= input_data[i] << (2 - bit_offset);
        } else {
            output_buffer[word_offset] |= input_data[i] >> (bit_offset - 2);
            output_buffer[word_offset + 1] |= input_data[i] << (16 - bit_offset + 2);
        }
    }
    
    uint8_t *packed_data = (uint8_t *) malloc(n_pixels * 14 / 16);

    for (int i = 0; i < n_pixels * 14 / 16; i++) {
        packed_data[i * 2] = (uint8_t) (output_buffer[i]) & 0xFF;
        packed_data[i * 2 + 1] = (uint8_t) ((output_buffer[i] >> 8) & 0xFF);
    }

	long x = n_pixels * 14 / 8;

    {
        FILE *stream;

        stream = fopen(output_path, "wb");
        fwrite(packed_data, x, 1, stream);
        fclose(stream);
    }

    return 0;
}

