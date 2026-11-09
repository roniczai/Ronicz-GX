// Original experiment: combinational vector integer ALU, not a complete GPU.
// Parameterized number of lanes, each 32 bits wide.
// op: 00=ADD (wraparound), 01=bitwise AND, 10=XOR, 11=MUL low 32 bits.
module gx_vector_alu #(
    parameter integer LANES = 8
) (
    input  logic [LANES*32-1:0] a,
    input  logic [LANES*32-1:0] b,
    input  logic [1:0]          op,
    output logic [LANES*32-1:0] y
);
    integer i;
    always_comb begin
        y = '0;
        for (i = 0; i < LANES; i = i + 1) begin
            case (op)
                2'b00: y[i*32 +: 32] = a[i*32 +: 32] + b[i*32 +: 32];
                2'b01: y[i*32 +: 32] = a[i*32 +: 32] & b[i*32 +: 32];
                2'b10: y[i*32 +: 32] = a[i*32 +: 32] ^ b[i*32 +: 32];
                2'b11: y[i*32 +: 32] = a[i*32 +: 32] * b[i*32 +: 32];
            endcase
        end
    end
endmodule

