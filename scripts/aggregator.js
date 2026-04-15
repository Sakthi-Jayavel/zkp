import { buildPoseidon } from "circomlibjs";

async function main() {

    const poseidon = await buildPoseidon();

    // 50 readings
    const readings = Array.from({ length: 50 }, (_, i) => i + 1);

    // Split into 5 batches
    const batches = [];
    for (let i = 0; i < 5; i++) {
        const batch = readings.slice(i * 10, (i + 1) * 10);
        const sum = batch.reduce((a, b) => a + b, 0);
        batches.push(sum);
    }

    // Total
    const total = batches.reduce((a, b) => a + b, 0);

    // Hash
    const hash = poseidon(batches);

    console.log("Batches:", batches);
    console.log("Total:", total);
    console.log("Hash:", poseidon.F.toString(hash));
}

main();
