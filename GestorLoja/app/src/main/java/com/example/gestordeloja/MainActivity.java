package com.example.gestordeloja;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btnVendas, btnEstoque, btnFinanceiro, btnRH, btnRelatorios;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnVendas = findViewById(R.id.btnVendas);
        btnEstoque = findViewById(R.id.btnEstoque);
        btnFinanceiro = findViewById(R.id.btnFinanceiro);
        btnRH = findViewById(R.id.btnRH);
        btnRelatorios = findViewById(R.id.btnRelatorios);

        // Ações futuras podem ser adicionadas aqui
    }
}
