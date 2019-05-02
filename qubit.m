A=[-pi/4 pi/4 0];
B=[0 pi*22/45 pi/12];
policylen=4;
policy=[1,1,1,1];
epi=500;
psch=([1,-1i]/sqrt(2))';
state=zeros(epi,1);
fl=epi;
pstate=zeros(epi+1,1);
while epi>0
    t=fl-epi+1;
    k=mod(t,policylen)+1;
    gc=policy(mod(t,policylen)+1);
    if mod(gc,2)==1
        g=A;
    else
        g=B;
    end
    game=U(g);
    psch=game*psch;
    r=psch(1,:);
    l=psch(2,:);
    pr=[0,r];
    pl=[l,0];
    psch=[pr;pl];
    le=floor(length(psch)/2);
    pbl=0;
    
    for q=1:le
        pbl=pbl+(abs(psch(1,q))^2+abs(psch(2,q))^2);
        pstate(q)=abs(psch(1,q))^2+abs(psch(2,q))^2;
    end
    pbr=0;
    for q=length(psch)-le+1:length(psch)
        pbr=pbr+(abs(psch(1,q))^2+abs(psch(2,q))^2);
        pstate(q)=abs(psch(1,q))^2+abs(psch(2,q))^2;
    end
    state(t)=(pbr-pbl)/(pbr+pbl);
    epi=epi-1;
end
plot(state');hold on
function u=U(x)
u=[0,0;0,0];
u(1)=exp(1i*x(1))*cos(x(2));
u(2)=-exp(-1i*x(3))*sin(x(2));
u(3)=exp(1i*x(3))*sin(x(2));
u(4)=exp(-1i*x(1))*cos(x(2));
end
