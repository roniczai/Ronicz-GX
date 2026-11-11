// Independent deterministic simulation tests for the programmable GX-Mini core.
`timescale 1ns/1ps
module tb_gx_program_core;
    reg clk = 0;
    reg reset = 1;
    wire done;
    wire [4:0] pc;
    integer i;
    reg [31:0] expected [0:3];
    reg [31:0] vals [0:3];
    gx_program_core dut(.clk(clk), .reset(reset), .done(done), .pc(pc));
    always #5 clk = ~clk;

    function [15:0] r;
        input [3:0] op;
        input [2:0] rd, ra, rb;
        begin r = {op, rd, ra, rb, 3'b000}; end
    endfunction

    function [15:0] m;
        input [3:0] op;
        input [2:0] rd;
        input [7:0] imm;
        begin m = {op, rd, 1'b0, imm}; end
    endfunction

    task release_reset;
        begin
            reset = 1;
            @(posedge clk);
            @(negedge clk);
            reset = 0;
        end
    endtask

    task run_and_check;
        input integer instr_count;
        begin
            repeat (instr_count + 2) @(negedge clk);
            if (done !== 1'b1)
                $fatal(1, "Program did not halt");
            for (i = 0; i < 4; i = i + 1)
                if (dut.data_mem[i][2] !== expected[i])
                    $fatal(1, "lane=%0d expected=%0d actual=%0d",
                           i, expected[i], dut.data_mem[i][2]);
        end
    endtask

    initial begin
        // Program 1: result[lane] = a[lane] * b[lane] + 7.
        dut.instr_mem[0] = m(4'h6,3'd1,8'd0);
        dut.instr_mem[1] = m(4'h6,3'd2,8'd1);
        dut.instr_mem[2] = r(4'h3,3'd3,3'd1,3'd2);
        dut.instr_mem[3] = m(4'h1,3'd4,8'd7);
        dut.instr_mem[4] = r(4'h2,3'd5,3'd3,3'd4);
        dut.instr_mem[5] = m(4'h7,3'd5,8'd2);
        dut.instr_mem[6] = 16'hF000;
        dut.data_mem[0][0] = 2; dut.data_mem[0][1] = 11; expected[0] = 29;
        dut.data_mem[1][0] = 3; dut.data_mem[1][1] = 13; expected[1] = 46;
        dut.data_mem[2][0] = 5; dut.data_mem[2][1] = 17; expected[2] = 92;
        dut.data_mem[3][0] = 7; dut.data_mem[3][1] = 19; expected[3] = 140;
        release_reset();
        run_and_check(7);
        $display("PASS: GX-Mini vector multiply-add: [29,46,92,140]");

        // Program 2: exercise addition overflow and XOR.
        dut.instr_mem[0] = m(4'h6,3'd0,8'd0);
        dut.instr_mem[1] = m(4'h6,3'd1,8'd1);
        dut.instr_mem[2] = r(4'h2,3'd2,3'd0,3'd1);
        dut.instr_mem[3] = r(4'h4,3'd3,3'd2,3'd1);
        dut.instr_mem[4] = m(4'h7,3'd3,8'd2);
        dut.instr_mem[5] = 16'hF000;
        vals[0] = 32'hFFFFFFFF;
        vals[1] = 32'h00000000;
        vals[2] = 32'h00000006;
        vals[3] = 32'h80000000;
        for (i = 0; i < 4; i = i + 1) begin
            dut.data_mem[i][0] = vals[i];
            dut.data_mem[i][1] = 2;
            expected[i] = (vals[i] + 32'd2) ^ 32'd2;
        end
        release_reset();
        run_and_check(6);
        $display("PASS: GX-Mini integer overflow and XOR on 4 lanes");
        $display("PASS: programmable four-lane simulated compute core");
        $finish;
    end
endmodule

