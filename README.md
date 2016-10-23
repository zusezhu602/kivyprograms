# kivyprograms
<h1>  Satcomapp</h1>
<h2>    satcomapp20101023</h2>
<h3>      frequency calculation</h3>
<span>
<h5>      界面初始化：fre_shift 默认下为1750；fre_interval 默认下为5；land_emit, plane_emit与plane_receive 为disabled，只可以显示数据，land_reveive为输入数据接口，初始为绿底。</h5>
<h5>      计算方法：只需要输入land_receive，点击calculate，先对fre_shift和fre_interval是否为空进行判断，若为空，使用默认值；再对land_receive进行判断，为空或超出ku范围，均在notice栏中报错，且颜色变为红色；若一切无错，点击计算，可得到相应结果。</h5>
</span>

