pragma circom 2.0.0;

include "circomlib/circuits/poseidon.circom";
include "circomlib/circuits/comparators.circom";

template BatchAggregateCheck(nBits) {

    signal input b1;
    signal input b2;
    signal input b3;
    signal input b4;
    signal input b5;

    signal input hash;
    signal input threshold;

    // Hash check
    component h = Poseidon(5);
    h.inputs[0] <== b1;
    h.inputs[1] <== b2;
    h.inputs[2] <== b3;
    h.inputs[3] <== b4;
    h.inputs[4] <== b5;

    hash === h.out;

    // Total
    signal total;
    total <== b1 + b2 + b3 + b4 + b5;

    // Threshold check
    component cmp = GreaterEqThan(nBits);
    cmp.in[0] <== total;
    cmp.in[1] <== threshold;

    signal output valid;
    valid <== cmp.out;
}

component main = BatchAggregateCheck(16);
