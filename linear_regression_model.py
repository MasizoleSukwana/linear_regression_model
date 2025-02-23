use rand::Rng;
use std::fs::File;
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let mut rng = rand::thread_rng();
    let num_samples = 100;

    let mut data = Vec::new();

    for _ in 0..num_samples {
        let x: f64 = rng.gen_range(-10.0..10.0);  // Random x in range [-10, 10]
        let noise: f64 = rng.gen_range(-1.0..1.0); // Small noise factor
        let y = 2.0 * x + 1.0 + noise;  // y = 2x + 1 + noise

        data.push((x, y));
    }

    // Print the dataset
    for (x, y) in &data {
        println!("{:.2}, {:.2}", x, y);
    }

    // Save to a CSV file
    let mut file = File::create("dataset.csv")?;
    writeln!(file, "x,y")?;
    for (x, y) in data {
        writeln!(file, "{},{}", x, y)?;
    }

    println!("Dataset saved to dataset.csv");
    
    Ok(())
}
