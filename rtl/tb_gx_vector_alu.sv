module tb_gx_vector_alu;
    localparam integer LANES = 8;
    logic [LANES*32-1:0] a, b, y;
    logic [1:0] op;
    gx_vector_alu #(.LANES(LANES)) dut (.a(a), .b(b), .op(op), .y(y));

    integer i;
    initial begin
        a = '0; b = '0; op = 0;
        for (i = 0; i < LANES; i = i + 1) begin
            a[i*32 +: 32] = i + 3;
            b[i*32 +: 32] = 2;
        end
        #1;
        for (i = 0; i < LANES; i = i + 1)
            if (y[i*32 +: 32] !== i + 5) $fatal(1, "ADD failure lane %0d", i);
        op = 2'b01; #1;
        for (i = 0; i < LANES; i = i + 1)
            if (y[i*32 +: 32] !== ((i + 3) & 2)) $fatal(1, "AND failure lane %0d", i);
        op = 2'b10; #1;
        for (i = 0; i < LANES; i = i + 1)
            if (y[i*32 +: 32] !== ((i + 3) ^ 2)) $fatal(1, "XOR failure lane %0d", i);
        op = 2'b11; #1;
        for (i = 0; i < LANES; i = i + 1)
            if (y[i*32 +: 32] !== ((i + 3) * 2)) $fatal(1, "MUL failure lane %0d", i);
        $display("PASS: 8-lane 32-bit integer vector ALU operations");
        $finish;
    end
endmodule

