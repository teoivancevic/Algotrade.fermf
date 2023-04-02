#include <bits/stdc++.h>
using namespace std;

using ld = long double;

const int inf=1e9;

string const url = "http://192.168.1.101:3000";

string const user = "fermf";
string const secret = "64f52091f316a1c27ce92ecb6fb3ebe5";

string const createTrade = "/createOrders/"+user+'/'+secret;

map < string, int > ind;
int curr;


mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

vector < pair < int, int > > edge;
vector<int> backEdge;
vector < __int128 > closeVal, volume;
vector < double > weight;
int n, m;

vector<ld> value;
vector<ld> pathVolume;
vector<ld> backVolume;
vector<pair<int, int>> parent;

void dfs(int cur) {
  vector<int> order(size(edge));
  iota(begin(order), end(order), 0);
  shuffle(begin(order), end(order), rng);
  for (int i : order) {
    auto [a, b] = edge[i];
    if (a != cur) continue;
    if (value[b] < -0.5) {
      parent[b] = pair{a, i};
      value[b] = value[a] * ((ld)closeVal[i] / 1e8);
      pathVolume[b] = min(pathVolume[a], (ld)volume[i]/(value[a]));
      if (pathVolume[b] == 0) {
        cerr << "why" << endl;
        value[b] = -1;
        pathVolume[b] = -1;
        continue;
      }
      cerr << pathVolume[b] << ' ' << i << ' ' << (ld)volume[i] << ' ' << value[b] << ' ' << pathVolume[a]<< endl;
      dfs(b);
    }
  }
}



void bestDeals() {
  cerr << "usao\n" << endl;
  vector<pair<ld, pair<int, ld>>> v;
  for (int i = 0; i < size(edge); ++i) {
    auto [a, b] = edge[i];
    ld bv = 1;
    int tmpx = b;
    int tmpp = parent[b].first;
    while (tmpp != -1) {
      int indeks = parent[tmpx].second;
      bv *= closeVal[backEdge[indeks]]/1e8;
      tmpx = tmpp;
      tmpp = parent[tmpx].first;
    }
    ld dt = (value[a] * ((ld)closeVal[i]/1e8)) * bv;
    ld pv = min(pathVolume[a], volume[i]/(value[a] * (ld)closeVal[i]/1e8));

    if (dt < 0.98 || value[a] <= 0) continue;
    ld cr = value[a] * ((ld)closeVal[i]/1e8);
    int xc = b;
    int xp = parent[b].first;
    while (xp != -1) {
        int indeks = parent[xc].second; 
        cr = cr * ((ld)closeVal[backEdge[indeks]]/1e8);
        pv = min(pv, volume[backEdge[indeks]]/cr);
        xc = xp;
        xp = parent[xc].first;
    }
    if (pv <= 0) continue;
//    cerr << dt - value[ind["USDT"]] << ' ' << pv << endl;
    v.emplace_back((dt - value[ind["USDT"]]) * pv, pair{i, pv});
  }
  sort(begin(v), end(v), greater<>());
  int x = 0;
  cerr << size(v) << endl;
  cout << v[x].first << ' ' << v[x].second.first << endl;
  cerr << edge[v[x].second.first].first << endl; 
  cerr << "Volume: " << v[x].second.second << endl;
  vector<int> pth;
  auto [a, b] = edge[v[x].second.first]; 
  while (a != ind["USDT"]) {
    pth.push_back(a);
    a = parent[a].first;
  }
  pth.push_back(a);
  reverse(begin(pth), end(pth));
  while (b != ind["USDT"]) {
    pth.push_back(b);
    b = parent[b].first;
  }
  pth.push_back(pth[0]);
  __int128 pv = (v[x].second.second * 3./4.);
  string req = "";
  vector<string> tmp;
  for (auto a : pth) {
    for (auto [key, val] : ind) {
      if (val == a) {
        cout << a << ' ' << key << ", ";
        tmp.push_back(key);
        break;
      }
    }
  }
  cout << endl;
  for (auto a : pth) cerr << a << ' ';
  cerr << endl;
  cerr << "STartVol: " << (long long)pv << endl;
  string prev = tmp[0];
  for (int i = 1; i < size(tmp); ++i) {
    if (i != 1) req += '|';
    req += prev+','+tmp[i]+','+to_string((long long)pv);
    for (int j = 0; j < size(edge); ++j) {
      if (edge[j] == pair{pth[i-1], pth[i]}) {
        pv = (pv * closeVal[j])/(__int128)(100000000); 
        if (edge[j] == pair{ind["USDT"], ind["STMX"]}) {
          cerr << "CV" << (long long)closeVal[j] << endl;
        }
        cout << (long long)pv << ' ' << (long long)volume[j] << ' ' << (long long)closeVal[j] << endl;
        break;
      }
    }
    prev = tmp[i];
  }
  cout << url + createTrade + '/' + req << endl; 
}


int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
  cout << setprecision(8) << fixed;
  cerr << setprecision(8) << fixed;
	string s;
	getline(cin, s);
	int br;
	string s1, s2;
	int x1, x2;
	__int128 val;
	bool p=0;
	while(true){
		getline(cin, s);
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
		val=0;
		while(s[br]>='0' && s[br]<='9'){
			val*=10;
			val+=s[br]-'0';
			br++;
		}
		if(p){
			volume.push_back(val);
		}
		else{
			edge.push_back({x1, x2});
			closeVal.push_back(val);
			weight.push_back(-log(val/1e8));
		}
	}
	n=ind.size();
	m=edge.size();
  
  cerr << ind.size() << endl;
  backEdge.resize(edge.size(), 0);
  value.resize(ind.size(), -1);
  pathVolume.resize(ind.size(), -1);
  parent.resize(ind.size(), {-1, 0});
  cerr << "Bruh" << endl;
  for (int i = 0; i < (int)size(edge); ++i) {
    for (int j = 0; j < (int)size(edge); ++j) {
      if (edge[i] == pair{edge[j].second, edge[j].first}) {
        backEdge[i] = j;
        break;
      }
    }
  }
  value[ind["USDT"]] = 1;
  pathVolume[ind["USDT"]] = 1000 * 1e8;
  dfs(ind["USDT"]);
  bestDeals(); 
/*	for(int i=0; i<edge.size(); i++){
		cout << edge[i].first << ' ' << edge[i].second << ' '  << weight[i] << '\n';
	}*/
	
	return 0;
}
