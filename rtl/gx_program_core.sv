// GX-Mini v0.1: four-lane lockstep 32-bit integer research compute core.
// Functional RTL only. Not a GPU, graphics pipeline, silicon, or FPGA prototype.
// Shared PC and instruction ROM; each lane has eight registers and local words.
module gx_program_core #(
    parameter integer LANES = 4
) (
    input  logic       clk,
    input  logic       reset,
    output logic       done,
    output logic [4:0] pc
);
    logic [15:0] instr_mem [0:15];
    logic [31:0] data_mem [0:LANES-1][0:15];
    logic [31:0] rf       [0:LANES-1][0:7];

    wire [15:0] ins = instr_mem[pc[3:0]];
    wire [3:0] op = ins[15:12];
    wire [2:0] rd = ins[11:9];
    wire [2:0] ra = ins[8:6];
    wire [2:0] rb = ins[5:3];
    wire [7:0] imm = ins[7:0];
    integer lane;
    integer reg_index;

    always @(posedge clk) begin
        if (reset) begin
            pc <= 0;
            done <= 0;
            for (lane = 0; lane < LANES; lane = lane + 1)
                for (reg_index = 0; reg_index < 8; reg_index = reg_index + 1)
                    rf[lane][reg_index] <= 0;
        end else if (!done) begin
            case (op)
                4'h0: begin end // NOP
                4'h1: for (lane = 0; lane < LANES; lane = lane + 1)
                    rf[lane][rd] <= {24'b0, imm};  // LDI rd, imm8
                4'h2: for (lane = 0; lane < LANES; lane = lane + 1)
                    rf[lane][rd] <= rf[lane][ra] + rf[lane][rb]; // ADD
                4'h3: for (lane = 0; lane < LANES; lane = lane + 1)
                    rf[lane][rd] <= rf[lane][ra] * rf[lane][rb]; // MUL lower 32
                4'h4: for (lane = 0; lane < LANES; lane = lane + 1)
                    rf[lane][rd] <= rf[lane][ra] ^ rf[lane][rb]; // XOR
                4'h6: for (lane = 0; lane < LANES; lane = lane + 1)
                    rf[lane][rd] <= data_mem[lane][imm[3:0]]; // LOAD rd,[imm]
                4'h7: for (lane = 0; lane < LANES; lane = lane + 1)
                    data_mem[lane][imm[3:0]] <= rf[lane][rd]; // STORE rd,[imm]
                4'hF: done <= 1; // HALT
                default: $fatal(1, "Unsupported GX-Mini opcode %x", op);
            endcase
            if (op != 4'hF)
                pc <= pc + 1'b1;
        end
    end
endmodule

