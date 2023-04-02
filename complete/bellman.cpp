#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <cassert>
#include <queue>
#include <cstring>
#include <ctime>
#include <cstdlib>

using namespace std;
typedef long long ll;

const int inf=1e9;
const int maxn=400;

map < string, int > ind;
int curr;



vector < pair < int, int > > edge;
vector < __int128 > close, volume;
vector < double > weight;
int n, m;

vector < int > red;
vector < int > ciklus;
vector < int > cik_edge;

__int128 balance;
int pocetak;


void print(__int128 x){
	vector < int > znam;
	if(x<0){
		cout << '-';
		x*=-1;
	}
	if(x==0){
		cout << 0;
	}
	while(x!=0){
		znam.push_back(x%10);
		x/=10;
	}
	reverse(znam.begin(), znam.end());
	for(int i : znam){
		cout << i;
	}
}


__int128 min(__int128 a, __int128 b) {
        if(a <= b) return a;
        else return b;
}

//typedef long long ll; 

__int128 get_min_vol(__int128 **mat_e, __int128 **mat_vol, vector<int> idx) {
	int n = idx.size();
	vector<__int128> vol;
	vol.push_back(mat_vol[idx[0]][idx[1]]);
//	cout << "pocinje " << endl;
	for(int i = 1; i < n - 1; ++i) {
//		print(mat_vol[idx[i]][idx[i + 1]]);
//		print(mat_e[idx[i]][idx[i + 1]]);
		vol.push_back(min(mat_vol[idx[i]][idx[i + 1]], vol.back() * mat_e[idx[i]][idx[i + 1]] / 100000000));
//		print(vol.back());
	}

//	cout << "sredina" << endl;
	__int128 ret = vol[0];
	__int128 div = 100000000;
	for(int i = 0; i < n - 1; ++i) {
//		cout << "ret" << endl;
//		print(ret);
//		cout << "div" << endl;
//		print(div);
		ret = min(ret, vol[i] / div * 100000000);
		div = div * mat_e[idx[i]][idx[i + 1]] / 100000000;
		
	}
	return ret;
}

vector < int > ms[maxn];
__int128 **ms_e, **ms_vol;

vector < int > cijeli_put;
vector < __int128 > pare;

ll update(){
	pare.clear();
	queue < int > q;
	q.push(pocetak);
	int dist[maxn];
	memset(dist, -1, sizeof(dist));
	dist[pocetak]=0;
	int x;
	while(!q.empty()){
		x=q.front();
		q.pop();
		for(int i=0; i<(int)ms[x].size(); i++){
			if(dist[ms[x][i]]==-1){
				dist[ms[x][i]]=dist[x]+1;
				q.push(ms[x][i]);
			}
		}
	}
	int ind=0, mini=1e9, ind1;
	for(int i=0; i<(int)ciklus.size(); i++){
		if(mini>dist[ciklus[i]]){
			ind=ciklus[i];
			ind1=i;
			mini=dist[ciklus[i]];
		}
	}
	vector < int > prvi_dio;
	x=ind;
	while(dist[x]>0){
		for(int i : ms[x]){
			if(dist[i]<dist[x]){
				x=i;
				break;
			}
		}
		prvi_dio.push_back(x);
	}
	reverse(prvi_dio.begin(), prvi_dio.end());
	cijeli_put=prvi_dio;
	for(int i=0; i<(int)ciklus.size(); i++){
		cijeli_put.push_back(ciklus[(ind1+i)%ciklus.size()]);
	}
	cijeli_put.push_back(ciklus[ind1]);
	reverse(prvi_dio.begin(), prvi_dio.end());
	for(int i : prvi_dio){
		cijeli_put.push_back(i);
	}
	
/*	cout << "putic " << endl;
	for(int i : cijeli_put){
		cout << i << ' ';
	}
	cout << endl;*/
	__int128 max_ulog=min(get_min_vol(ms_e, ms_vol, cijeli_put), balance);
//	cout << "max_ulog" << endl;
	__int128 na_kraju=max_ulog;


/*	__int128 provjeri=1e8;
	for(int i=0; i<cijeli_put.size()-1; i++){
		provjeri*=ms_e[cijeli_put[i]][cijeli_put[i+1]];
		provjeri/=1e8;
		assert(provjeri<=ms_vol[cijeli_put[i]][cijeli_put[i+1]]);
	}*/

	for(int i=0; i<cijeli_put.size()-1; i++){
//		print(ms_vol[cijeli_put[i]][cijeli_put[i+1]]);
		pare.push_back(max_ulog);
		max_ulog*=ms_e[cijeli_put[i]][cijeli_put[i+1]];
		max_ulog/=100000000;
	}
//	cout << "profit" << endl;
//	print(max_ulog);
//	print(na_kraju);

	return (na_kraju-max_ulog);
}


bool cmp(int a, int b){
	return (double)volume[a]/close[a]>(double)volume[b]/close[b];
}

bool bellman_ford(int x){
	ciklus.clear();
	cik_edge.clear();
	sort(red.begin(), red.end(), cmp);
	double dist[n];
	pair < int, int > anc[n];
	for(int i=0; i<n; i++){
		dist[i]=inf;
		anc[i]={-1, -1};
	}
	dist[x]=0;
	for(int i=0; i<n; i++){
		for(int j : red){
			if(dist[edge[j].first]+weight[j]<dist[edge[j].second]){
				anc[edge[j].second]={edge[j].first, j};
				dist[edge[j].second]=dist[edge[j].first]+weight[j];
			}
		}
		if(anc[x].first!=-1){
			break;
		}
	}
	if(anc[x].first==-1){
		return 0;
	}
	for(int i=0; i<n; i++){
		x=anc[x].first;
	}
	ciklus.clear();
	while(true){
		if(ciklus.size()>1 && x==ciklus[0]){
			break;
		}
		ciklus.push_back(x);
		cik_edge.push_back(anc[x].second);
		x=anc[x].first;
	}
/*	cout << "nasao cilus!\n";
	for(int i : ciklus){
		cout << i << ' ';
	}
	cout << '\n';*/
	return 1;
}

string rev[maxn];

int main(){
	srand(time(NULL));
	ms_vol=new __int128*[maxn];
	ms_e=new __int128*[maxn];
	for(int i=0; i<maxn; i++){
		ms_vol[i]=new __int128[maxn];
		ms_e[i]=new __int128[maxn];
	}
	balance=1000;
	balance*=100000000;
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	string s;
	getline(cin, s);
	int br;
	string s1, s2;
	int x1, x2;
	__int128 val;
	bool p=0;
	int tren=0;
	bool daljeee=0;
	while(true){
		getline(cin, s);
		if(daljeee){
			daljeee=0;
			continue;
		}
		if(s=="}"){
			break;
		}
		br=0;
		while(s[br]!='_'){
			br++;
		}
		if(s[br-2]=='m'){
			p=1;
		}
		br++;
		s1="";
		while(s[br]!=','){
			s1.push_back(s[br]);
			br++;
		}
		br++;
		s2="";
		while(s[br]!='"'){
			s2.push_back(s[br]);
			br++;
		}
		while(s[br]<'0' || s[br]>'9'){
			br++;
		}
		if(ind.find(s1)==ind.end()){
			ind[s1]=curr++;
		}
		if(ind.find(s2)==ind.end()){
			ind[s2]=curr++;
		}
		x1=ind[s1];
		x2=ind[s2];
		ms[x1].push_back(x2);
		val=0;
		while(s[br]>='0' && s[br]<='9'){
			val*=10;
			val+=s[br]-'0';
			br++;
		}
		if(p){
			if(!val){
//				cout << "brisem " << edge[tren].first << ' ' << edge[tren].second << endl;
				edge.erase(edge.begin()+tren);
				close.erase(close.begin()+tren);
				ms[x1].erase(find(ms[x1].begin(), ms[x1].end(), x2));
				if(tren&1){
//				cout << "brisem " << edge[tren-1].first << ' ' << edge[tren-1].second << endl;
					ms[x1].erase(find(ms[x1].begin(), ms[x1].end(), x2));
					edge.erase(edge.begin()+tren-1);
					close.erase(close.begin()+tren-1);
					volume.erase(volume.begin()+tren-1);
					tren--;
				}
				else{
//					cout << "brisem " << edge[tren].first << ' ' << edge[tren].second << endl;
					edge.erase(edge.begin()+tren);
					close.erase(close.begin()+tren);
					daljeee=1;
				}
				tren--;
			}
			else{
				ms_vol[x1][x2]=val;
				volume.push_back(val);
			}
			tren++;
		}
		else{
			ms_e[x1][x2]=val;
			edge.push_back({x1, x2});
			close.push_back(val);
			weight.push_back(-log(val/1e8));
		}
	}
	pocetak=ind["USDT"];
//	cout << "krecem od " << pocetak << endl;
	n=ind.size();
//	cout << n << endl;
	m=edge.size();
	for(int i=0; i<m; i++){
		red.push_back(i);
	}
	ll value=0;
	while(value<=0){
		if(!bellman_ford(rand()%n)){
			continue;
		}
		value=update();
	}
	for(auto it : ind){
		rev[it.second]=it.first;
	}
	for(int i=0; i<cijeli_put.size()-1; i++){
		if(i){
			cout << '|';
		}
		cout << rev[cijeli_put[i]] << "," << rev[cijeli_put[i+1]] << ',';
		print(pare[i]);
	}
	cout << '\n';
/*	for(int i=0; i<n; i++){
		bellman_ford(i);
	}*/
	return 0;
}
