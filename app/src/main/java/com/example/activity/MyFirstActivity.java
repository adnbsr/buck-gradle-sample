package com.example.activity;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;
import butterknife.Bind;
import butterknife.ButterKnife;

public class MyFirstActivity extends Activity {


  private final int helloId = R.id.hello;

  @Bind(R.id.hello) TextView helloView;

  @Override
  public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    ButterKnife.bind(this);

    helloView.setText("Hey");


  }
}
