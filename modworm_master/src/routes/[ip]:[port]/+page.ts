import { error} from '@sveltejs/kit';

export const ssr = false;

export async function load({ fetch, params }) {
	const port = params.port;
	const ip = params.ip;

	async function try_discover() {
		const response = await fetch(`http://127.0.0.1:5000/nmap/${ip}/${port}`);
		if (!response.ok) throw error(response.status, await response.json());
		const servers = await response.json();
		console.log(servers);
	
		for (const server of servers) {
			if (server.address === ip && server.port === port) return true;
		}
		return false;
	}

	return { discovered: try_discover(), ip, port};
}



