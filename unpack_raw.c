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

    uint8_t *input_data;
    long input_size;

    {
        FILE *stream;

        stream = fopen(input_path, "rb");

        fseek(stream, 0L, SEEK_END);
        input_size = ftell(stream);
        fseek(stream, 0L, SEEK_SET);

        input_data = (uint8_t *) malloc(input_size);
        fread(input_data, 1, input_size, stream);

        fclose(stream);
    }

    long n_pixels = input_size * 8 / 14;

    printf("Input size: %d - Pixel count: %d\n", input_size, n_pixels);

    long packed_size = input_size / 2;
    uint16_t *packed_data = (uint16_t *) malloc(packed_size);

    for (int i = 0; i < packed_size; i++) {
        packed_data[i] =
            (((uint16_t) input_data[i * 2])) |
            (((uint16_t) input_data[i * 2 + 1]) << 8);
    }

    uint16_t *output_buffer = (uint16_t *) malloc(n_pixels);

    for (int i = 0; i < n_pixels; i++) {
        long packed_idx = i * 14 / 16;
        long packed_off = i * 14 % 16;

        uint16_t res;

        if (packed_off <= 2) {
            res = (packed_data[packed_idx] >> (2 - packed_off)) & 0x3FFF;
        } else {
            res = ((packed_data[packed_idx] << (packed_off - 2)) & 0x3FFF)
                | (packed_data[packed_idx + 1] >> (16 - packed_off + 2));
        }

        output_buffer[i] = res;
    }

    {
        FILE *stream;

        stream = fopen(output_path, "wb");
        fwrite(output_buffer, n_pixels, 2, stream);
        fclose(stream);
    }

    return 0;
}
