<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class ProductSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        $timestamp = \Carbon\Carbon::now()->toDateTimeString();
        DB::connection('mysql')->table('products')->insert([
            'name' => 'client',
            'created_at'=> $timestamp,
            'updated_at' => $timestamp,
        ]);
    }
}
